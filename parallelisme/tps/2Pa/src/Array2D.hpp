#include <vector>
#include <cstdlib>
#include "Point.hpp"

// simple classe pour un tableau 2D
template<class T>
class Array2D {
    std::vector<T> vector;
    size_t sX;
public:
    Array2D() : vector(0), sX(0) {}
    Array2D(size_t cols, size_t rows) : vector (cols*rows), sX(cols) {}
    Array2D(size_t cols, size_t rows, T init) : vector (cols*rows, init), sX(cols) {}
    T& operator()(size_t xCoord, size_t yCoord) {
        return vector.at(yCoord*sX+xCoord);
    }
    T* data(){ return vector.data(); }
    size_t sizeX(){ return sX;  }
    size_t sizeY(){ return vector.size()/sX;  }
    void resize(size_t c, size_t r){
        vector.resize(r*c);
        sX = c;
    }
    void unsafeSwap(Array2D<T> &otherArray){ otherArray.vector.swap(vector); }
    std::vector<T>& unsafeVector(){ return vector; }

    //Mes méthodes personnelles
    T& operator()(Point p) {
        return vector.at(p.y()*sX+p.x());
    }
    bool isIn(Point p){ return (p.x() < sX) && (p.y() < vector.size()/sX); }
    std::vector<T> getVector(){ return vector; }

    void show(){ 
	int c= 0;
	std::cout << "" << std::endl;
	for(int i= vector.size()-1; i >= 0; i--){
		std::cout << vector.at(i) << " " ;
		c++;
		if(c == sX){
			c= 0;
		std::cout << std::endl;
		}
	}
    }
   T max(){
	T max= 0;
	for(T i: vector){
		if(i > max){
			max= i;
		}
	}
	return max;
   }
   void setVector(std::vector<T> v){ vector= v;}
   size_t getColumn(){ return sX;}
};
