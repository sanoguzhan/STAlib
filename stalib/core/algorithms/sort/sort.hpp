#ifndef __SORT_HPP
#define __SORT_HPP

#include<iostream>
#include<vector>
#include <omp.h>
namespace sta{

template<typename T>
void swap(T *rh, T *lh){
    T temp = *rh;
    *rh = *lh;
    *lh = temp;
}

template < typename T>
void bubble_sort(std::vector<T> &vec){
    
    size_t n = vec.size();
    bool exec;
    for(size_t i=0; i < n-1; i++){
        exec = true;
        for(size_t j=0; j < n-i-1; j++){
            if(vec.at(j) > vec.at(j+1)){
                swap(&vec[j], &vec[j+1]);
                exec = false;
            }
        }

        if(exec){   
            i = vec.size();
        }
    }
}




}
#endif 
