#ifndef __SEARCH_HPP
#define __SEARCH_HPP

#include<iostream>
#include<vector>

/**
 * Binary Search Function Template.
 *
 * @param vec: Sorted Array which the elements is searched.
 * @param token: Searched item
 * @return index of searched if exist in vector else -1.
 */
template <typename T>
int binary_search(std::vector<T> &vec, T token){
    size_t lower = 0;
    size_t upper = vec.size() - 1;

    while(lower <= upper){
        int mid = ((upper - lower) / 2) + lower;
        if(token > vec.at(mid)){
            lower = mid +1;
        }else if(token < vec.at(mid)){
            upper = mid -1; 
        }else{
            return mid;
        }
   }
   return -1;
}

#endif 
