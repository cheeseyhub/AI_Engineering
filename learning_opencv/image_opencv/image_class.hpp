#include <iostream>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

#ifndef CLASS
#define CLASS

class image_class
{
public:
    std::string path;
    cv::Mat img;
    image_class(std::string imagepath);
    void open_window_normal();

    void wait_close_window();
};

#endif