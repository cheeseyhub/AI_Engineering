#include <opencv2/core.hpp>
#include <opencv2/video.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <stdio.h>

int main()
{

    cv::Mat frame, prevFrame, gray, prevGray, diff, thresh;
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

    cv::namedWindow("Motion Heatmap", cv::WINDOW_NORMAL);
    cv::namedWindow("Motion mask", cv::WINDOW_NORMAL);
    for (;;)
    {
        cap.read(frame);
        cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
        cv::GaussianBlur(gray, gray, cv::Size(21, 21), 0);

        if (frame.empty())
        {
            std::cerr << "Error! blank frame grabbed \n";
            break;
        }
        if (!prevGray.empty())
        {
            cv::absdiff(prevGray, gray, diff);
            cv::threshold(diff, thresh, 25, 255, cv::THRESH_BINARY);

            cv::Mat motionColored;
            cv::applyColorMap(diff, motionColored, cv::COLORMAP_JET);

            cv::imshow("Motion Heatmap", motionColored);
            cv::imshow("Motion mask", thresh);
        }
        gray.copyTo(prevGray);

        if (cv::waitKey(5) >= 0)
        {
            break;
        }
    }

    return 0;
}