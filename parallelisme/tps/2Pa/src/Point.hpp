#if !defined(__POINT__)
#define __POINT__

	// simple classe pour un tableau 2D
	class Point {
		int X;
		int Y;
	public:
	    Point() : X(0), Y(0) {}
	    Point(int newX, int newY) : X(newX), Y(newY){}
	    int x(){ return X; }
	    int y(){ return Y; }
	    Point plus(int newX, int newY){ return Point(X+newX, Y+newY); }
	    Point plus(Point p){ return Point(X+p.x(), Y+p.y()); }
	    void show(){ std::cout << "(" << X << "," << Y << ")" << std::endl;}
	};

#endif


