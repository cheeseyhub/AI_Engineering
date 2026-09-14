#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include "image_class.hpp"

using namespace cv;
int main()
{
    image_class image("image.jpg");
    image.open_window_normal();
    image.wait_close_window();
    return 0;
}