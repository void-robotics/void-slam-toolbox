#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"

using std::placeholders::_1;

class ReadingLaser : public rclcpp::Node {

public:
	ReadingLaser(): Node("Reading_laser"){ 

		auto default_qos = rclcpp::QoS(rclcpp::SystemDefaultsQoS());

		subscription_ = this->create_subscription<sensor_msgs::msg::LaserScan>(
			"laser_scan",default_qos,
			std::bind(&ReadingLaser::topic_callback,  this, _1));
	}


private:
	void topic_callback(const sensor_msgs::msg::LaserScan::SharedPtr _msg) {  
	// # _msg is the variable consisting the shared Pointer
		RCLCPP_INFO(this->get_logger(), "I heard: '%f' '%f'", _msg->ranges[0],
			_msg->ranges[100]);

	}
	rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_;

};


int main(int argc, char *argv[]) {

	rclcpp::init(argc, argv);
	auto node = std::make_shared<ReadingLaser>();
	RCLCPP_INFO(node->get_logger(),"Hola my friends");
	rclcpp::spin(node);
	rclcpp::shutdown();
	return 0;

}