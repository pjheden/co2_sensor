import servo as s
import co2_sensor as co2
import time
import datetime

def save_data(oxygen, angle):
	now = datetime.datetime.now().isoformat()
	print("timestamp", now)
	f = open("./www/static/data.csv","a")
	f.write(now + "," + str(oxygen) + "," + str(angle) + "\n")
	f.close()


def main():
	servo = s.Servo()
	sensor = co2.Co2Sensor()
	treshold = 900

	while True:
		oxygen = sensor.sense()
		if oxygen > treshold:
			servo.SetAngle(0)
		else:
			servo.SetAngle(90)

		save_data(oxygen, servo.getRotation())

		# time.sleep(300) # 5 min
		time.sleep(10) # 5 seconds

if __name__ == '__main__':
	main()
	# save_data(10, 90)
