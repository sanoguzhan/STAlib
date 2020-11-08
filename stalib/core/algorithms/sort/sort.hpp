#ifndef __SORT_HPP
#define __SORT_HPP

#include<iostream>
#include<vector>

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


template<typename T>
void merge(std::vector<T> &left, 
            std::vector<T> &right,
            std::vector<T> &vec)
            {

    size_t nLeft = left.size();
    size_t nRight = right.size();

    size_t i=0, j=0, k=0;

    while (j < nLeft && k < nRight)
    {
        if(left.at(j) < right.at(k)){
            vec[i] = left.at(j);
            j++;
        }else{
            vec[i] = right.at(k);
            k++;
        }
        i++;
    }
    
    while( j < nLeft){
        vec[i] = left.at(j);
        j++;
        i++;
    }
    while(k < nRight){
        vec[i] = right.at(k);
        k++;
        i++;
    }

}

template<typename T>
void merge_sort(std::vector<T> &vec){
    if (vec.size() <= 1) return;
    std::vector<T> left;
    std::vector<T> right;
    size_t mid = vec.size() /2;
    for (size_t j = 0; j < mid;j++)
        left.push_back(vec[j]);
    for (size_t j = 0; j < (vec.size()) - mid; j++)
        right.push_back(vec[mid + j]);

    merge_sort(left);
    merge_sort(right);
    merge(left,right,vec);
    
}


}
#endif 
