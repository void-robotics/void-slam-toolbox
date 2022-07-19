#include <chrono>
#include <functional>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class MovingRobot : public rclcpp::Node {
public:
  MovingRobot() : Node("moving_robot"), count_(0) {
    // How many time do we have publisher specific message, count
    publisher_ =
        this->create_publisher<geometry_msgs::msg::Twist>("/dolly/cmd_vel", 10);
        // This method extends from Node class
    timer_ = this->create_wall_timer(
      // This timer will publish the in message every 500 ms 
        500ms, std::bind(&MovingRobot::timer_callback, this));
    // we have to bind the callback and this callback will bind the timer to call the publisher in a very specific interval of time


  }

private:
  void timer_callback() {
    auto message = geometry_msgs::msg::Twist();
    message.linear.x = 0.5;
    message.angular.z = 0.3;
    RCLCPP_INFO(this->get_logger(), "Publishing: '%f.2' and %f.2",
                message.linear.x, message.angular.z);
    publisher_->publish(message);
    // This is wehere the msg will be published 
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MovingRobot>());
  rclcpp::shutdown();
  return 0;
}