#include "geometry_msgs/msg/twist.hpp"    // Twist
#include "rclcpp/rclcpp.hpp"              // ROS Core Libraries
#include "sensor_msgs/msg/laser_scan.hpp" // Laser Scan

using std::placeholders::_1;


class ObstacleAvoidance : public rclcpp::Node {
public:
  ObstacleAvoidance() : Node("ObstacleAvoidance") { 
  	// Contructor of class obstacle avoidance

    auto default_qos = rclcpp::QoS(rclcpp::SystemDefaultsQoS());
    subscription_ = this->create_subscription<sensor_msgs::msg::LaserScan>(
    	// "this->" is a value defined in the node class. since we are inheriting from the node class we can use the this pointer 
    	// to directly point / create a subscriber or a publisher

        "laser_scan", default_qos,
        std::bind(&ObstacleAvoidance::topic_callback, this, _1));
    publisher_ =
        this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);
  }


private:
  void topic_callback(const sensor_msgs::msg::LaserScan::SharedPtr _msg) {
    // 200 readings, from right to left, from -57 to 57 degress
    // calculate new velocity cmd
    float min_dist = 10;
    for (int i = 0; i < 300; i++) {
      float current = _msg->ranges[i];
      if (current < min_dist) {
        min_dist = current;
      }
    }
    // In one iteration it checks the 200 lasers and realises the minimum distance of object to a particular laser
    // This happens for each call back

    auto message = this->calculateVelMsg(min_dist);
    publisher_->publish(message);
	}
	geometry_msgs::msg::Twist calculateVelMsg(float distance) {
	    auto msg = geometry_msgs::msg::Twist();
	    // logic
	    RCLCPP_INFO(this->get_logger(), "Distance is: '%f'", distance);
	    if (distance < 1) {
	      // turn around
	      msg.linear.x = -0.6;
	      msg.angular.z = 0.5;
	    } else {
	      // go straight ahead
	      msg.linear.x = 0.6;
	      msg.angular.z = 0;
	    }
	    return msg;
	  }

	  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
	  rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_;
	};	



int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ObstacleAvoidance>()); 
  // this is where the constructor is called sinc
  rclcpp::shutdown();
  return 0;
}
