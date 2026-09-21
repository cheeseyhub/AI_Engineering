#include <opencv2/core.hpp>
#include <opencv2/video.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <stdio.h>

int main()
{

    cv::Mat frame;
    cv::VideoCapture cap;

    int deviceID = 0;
    int apiID = cv::CAP_ANY;

    cap.open(deviceID, apiID);

    if (!cap.isOpened())
    {
        std::cerr << "Error : Unable to open the camera \n";
        return -1;
    }

    std::cout << "Start grabbing " << std::endl
              << "Press any key to terminate " << std::endl;

    cv::namedWindow("Display", cv::WINDOW_NORMAL);
    for (;;)
    {
        cap.read(frame);
        if (frame.empty())
        {
            std::cerr << "Error! blank frame grabbed \n";
            break;
        }

        imshow("Display", frame);

        if (cv::waitKey(5) >= 0)
        {
            break;
        }
    }

    return 0;
}