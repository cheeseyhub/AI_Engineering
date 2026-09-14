#include <iostream>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

#include "image_class.hpp"

using namespace cv;
image_class::image_class(std::string imagepath)
{
    if (!imagepath.empty())
    {
        this->path = cv::samples::findFile(imagepath);
        this->img = imread(imagepath, IMREAD_COLOR);
    }
    else
    {
        std::cout << "Could not read the image Path " << imagepath << std::endl;
    }
}

void image_class::open_window_normal()
{
    namedWindow("Display Window", WINDOW_NORMAL);
    imshow("Display Window", img);
}
void image_class::wait_close_window()
{
    while (true)
    {
        int k = waitKey(0);

        if (k == 'q')
            break;
    }
}