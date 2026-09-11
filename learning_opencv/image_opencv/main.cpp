#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
int main()
{

    std::string image_path = samples::findFile("image.jpg");
    Mat img = imread(image_path, IMREAD_COLOR);

    if (img.empty())
    {
        std::cout << "Could not read the image:  " << image_path << std::endl;

        return 1;
    }

    namedWindow("Display Window", WINDOW_NORMAL);

    cvtColor(img, img, COLOR_BGR2GRAY);
    imshow("Display Window", img);

    while (true)
    {
        int k = waitKey(0);

        if (k == 'q')
        {
            break;
        }
    }
    destroyAllWindows();
    return 0;
}