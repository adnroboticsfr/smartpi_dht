import time
import struct
import mmap
import os

class DHTSensor:
    GPIO_BASE = 0x3F200000  # GPIO base address
    BLOCK_SIZE = 4096  # Memory block size for MMIO
    GPIO_SET_OFFSET = 0x1C  # Offset for setting GPIO pins
    GPIO_CLR_OFFSET = 0x28  # Offset for clearing GPIO pins
    GPIO_LEV_OFFSET = 0x34  # Offset for reading GPIO pin level

    def __init__(self, sensor_type="DHT22", pin=4):
        self.sensor_type = sensor_type
        self.pin = pin

        self.mem_fd = os.open('/dev/mem', os.O_RDWR | os.O_SYNC)
        self.gpio_mem = mmap.mmap(self.mem_fd, self.BLOCK_SIZE, mmap.MAP_SHARED,
                                  mmap.PROT_READ | mmap.PROT_WRITE, offset=self.GPIO_BASE)

        self.gpio = struct.Struct("L")

    def _gpio_set_mode_output(self):
        reg_offset = (self.pin // 10) * 4
        shift = (self.pin % 10) * 3
        data = self._read_reg(reg_offset)
        data &= ~(7 << shift)
        data |= (1 << shift)
        self._write_reg(reg_offset, data)

    def _gpio_set_mode_input(self):
        reg_offset = (self.pin // 10) * 4
        shift = (self.pin % 10) * 3
        data = self._read_reg(reg_offset)
        data &= ~(7 << shift)
        self._write_reg(reg_offset, data)

    def _gpio_set_pin(self):
        reg_offset = self.GPIO_SET_OFFSET
        self._write_reg(reg_offset, 1 << self.pin)

    def _gpio_clear_pin(self):
        reg_offset = self.GPIO_CLR_OFFSET
        self._write_reg(reg_offset, 1 << self.pin)

    def _gpio_read_pin(self):
        reg_offset = self.GPIO_LEV_OFFSET
        value = self._read_reg(reg_offset)
        return (value >> self.pin) & 1

    def _read_reg(self, offset):
        self.gpio_mem.seek(offset)
        return self.gpio.unpack(self.gpio_mem.read(4))[0]

    def _write_reg(self, offset, value):
        self.gpio_mem.seek(offset)
        self.gpio_mem.write(self.gpio.pack(value))

    def _read_sensor_data(self):
        self._gpio_set_mode_output()
        self._gpio_clear_pin()
        time.sleep(0.018)

        self._gpio_set_mode_input()
        time.sleep(0.02)

        data = []
        for i in range(40):
            while self._gpio_read_pin() == 0:
                pass
            start_time = time.time()

            while self._gpio_read_pin() == 1:
                pass
            duration = time.time() - start_time
            data.append(1 if duration > 0.00005 else 0)

        humidity = self._bits_to_bytes(data[0:8]) + self._bits_to_bytes(data[8:16]) * 0.1
        temperature = self._bits_to_bytes(data[16:24]) + self._bits_to_bytes(data[24:32]) * 0.1

        checksum = self._bits_to_bytes(data[32:40])
        if checksum == ((self._bits_to_bytes(data[0:8]) + self._bits_to_bytes(data[8:16]) +
                         self._bits_to_bytes(data[16:24]) + self._bits_to_bytes(data[24:32])) & 0xFF):
            return temperature, humidity
        else:
            return None, None

    @staticmethod
    def _bits_to_bytes(bits):
        byte = 0
        for bit in bits:
            byte = (byte << 1) | bit
        return byte

    def read(self):
        return self._read_sensor_data()

    def close(self):
        self.gpio_mem.close()
        os.close(self.mem_fd)
