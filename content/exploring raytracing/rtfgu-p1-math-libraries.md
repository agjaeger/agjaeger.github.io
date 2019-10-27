title: Working through "Raytracing From the Ground Up" Part 1: Introduction
slug: rtgu-p1-math-libaries
category: exploring raytracing
date: 2019-04-08
modified: 2019-04-08
summary: 

To learn Raytracing, I am working through Raytracing from the Ground Up by Kevin Suffern.



First, we begin by defining a few math classes and using stb_image_write to output a PNG.


```cpp
namespace math {
    struct Normal3 {
        double x = 0.0;
        double y = 0.0;
        double z = 0.0;
    };

    Normal3 operator+ (const Normal3& normalA, const Normal3& normalB);
    Vector3 operator+ (const Vector3& vec, const Normal3& normalA);
    Vector3 operator+ (const Normal3& normalA, const Vector3& vec);

    double operator* (const Normal3& normal, const Vector3& vec);    
    double operator* (const Vector3& vec, const Normal3& normal);
    Normal3 operator* (const Normal3& normal, double scalar);
    Normal3 operator* (double scalar, const Normal3& normal);
    
    std::ostream& operator<<(std::ostream& os, const Normal3& normal);
    
    double sqlength (const Vector3& vec);
    double length (const Vector3& vec);

    Normal3 negate (const Normal3& norm);
    
    double dot (const Vector3& vecA, const Vector3& vecB);
    Vector3 cross (const Vector3& vecA, const Vector3& vecB);
};


namespace math {
    struct Point3 {
        double x = 0.0;
        double y = 0.0;
        double z = 0.0;
    };

    Point3 operator+ (const Point3& pointA, const Vector3& vecB);
    Point3 operator+ (const Vector3& vecA, const Point3& pointB);
    Vector3 operator- (const Point3& pointA, const Point3& pointB);
    
    double distance (const Point3& pointA, const Point3& pointB);
    double sqDistance (const Point3& pointA, const Point3& pointB);
    
    std::ostream& operator<<(std::ostream& os, const Vector3& vec);
    
    double sqlength (const Vector3& vec);
    double length (const Vector3& vec);
};

namespace math {
    struct Vector3 {
        double x = 0.0;
        double y = 0.0;
        double z = 0.0;
    };

    Vector3 operator+ (const Vector3& vecA, const Vector3& vecB);
    Vector3 operator- (const Vector3& vecA, const Vector3& vecB);
    Vector3 operator* (const Vector3& vec, double scalar);
    Vector3 operator* (double scalar, const Vector3& vec);    
    Vector3 operator/ (const Vector3& vec, double scalar);
    std::ostream& operator<<(std::ostream& os, const Vector3& vec);
    
    double sqlength (const Vector3& vec);
    double length (const Vector3& vec);

    double dot (const Vector3& vecA, const Vector3& vecB);
    Vector3 cross (const Vector3& vecA, const Vector3& vecB);
};
```
