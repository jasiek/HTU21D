from smbus import SMBus

I2C_ADDR = 0x40
CMD_TRIG_TEMP_HM = 0xE3
CMD_TRIG_HUMID_HM = 0xE5
CMD_TRIG_TEMP_NHM = 0xF3
CMD_TRIG_HUMID_NHM = 0xF5
CMD_WRITE_USER_REG = 0xE6
CMD_READ_USER_REG = 0xE7
CMD_RESET = 0xFE
    
class HTU21D:
    def __init__(self, busno):
        self.bus = SMBus(busno)

    def read_temperature(self):
        self.reset()
        msb, lsb, crc = self.bus.read_i2c_block_data(I2C_ADDR, CMD_TRIG_TEMP_HM, 3)
        return -46.85 + 175.72 * (msb * 256 + lsb) / 65536
     
    def read_humidity(self):
        self.reset()
        msb, lsb, crc = self.bus.read_i2c_block_data(I2C_ADDR, CMD_TRIG_HUMID_HM, 3)
        return -6 + 125 * (msb * 256 + lsb) / 65536.0

    def reset(self):
        self.bus.write_byte(I2C_ADDR, CMD_RESET)

if __name__ == '__main__':
    htu = HTU21D(1)
    print htu.read_temperature()
    print htu.read_humidity()

