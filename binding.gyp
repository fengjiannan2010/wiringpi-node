{
  'targets': [
    {
      'target_name': 'WiringPi',
      'sources': [
        'src/addon.cc',
        
        'src/wiringPi.cc',
        'src/softPwm.cc',
        'src/softServo.cc',
        'src/softTone.cc',
        'src/wiringPiI2C.cc',
        'src/wiringPiSPI.cc',
        'src/wiringSerial.cc',
        'src/wiringShift.cc',
        'src/wiringPiISR.cc',
        'src/wpi.cc',
        
        'src/devlib/devlib.cc',
        'src/devlib/ds1302.cc',
        'src/devlib/gertboard.cc',
        'src/devlib/lcd.cc',
        'src/devlib/lcd128x64.cc',
        'src/devlib/maxdetect.cc',
        'src/devlib/piFace.cc',
        'src/devlib/piGlow.cc',
        'src/devlib/piNes.cc',
      ],
      'include_dirs': [
        'WiringPi/wiringPi',
        'WiringPi/devLib'
      ],
      'libraries': [
        '<!(pwd)/WiringPi/wiringPi/libwiringPi.a',
        '<!(pwd)/WiringPi/devLib/libwiringPiDev.a'
      ],
      'cflags': [
        '-Wall'
      ]
    }
  ]
}
