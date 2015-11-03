
#ifndef __MOTORLIB_H__
#define __MOTORLIB_H__

Adafruit_MotorShield motor_set_1 = Adafruit_MotorShield(0x67);
Adafruit_MotorShield motor_set_2 = Adafruit_MotorShield(0x61);
Adafruit_MotorShield motor_set_3 = Adafruit_MotorShield(0x60);
Adafruit_MotorShield motor_set_4 = Adafruit_MotorShield(0x66);

Adafruit_MotorShield* motor_sets[] = {
    &motor_set_1,
    &motor_set_2,
    &motor_set_3,
    &motor_set_4,
};

class CrazyMotor {
    Adafruit_DCMotor* motor_;
    unsigned long expiration_;

public:
    CrazyMotor() {}

    void init(Adafruit_DCMotor* motor) {
        motor_ = motor;
        reset();
    }

    void loop() {
        auto now = millis();
    }

    void reset() {
        // Expires in between 10 and 20 seconds.
        expiration_ = random(10, 20) * 1e6 + millis();
        motor_->run(random(FORWARD, BACKWARD + 1));
        motor_->setSpeed(random(1, 256));
        motor_->run(RELEASE);
    }

    void stop() {
        motor_->setSpeed(0);
        motor_->run(BRAKE);
    }
};

CrazyMotor motors[16];

void init_motors() {
    int motor = 0;
    for (int motor_set = 0; motor_set < 4; ++motor_set) {
        for (int shield_motor = 1; shield_motor <= 4; ++shield_motor) {
            motors[motor].init(motor_sets[motor_set]->getMotor(shield_motor));
        }
    }
}

void loop_motors() {
    for (int motor = 0; motor < 16; ++motor) {
        motors[motor].loop();
    }
}

#endif
