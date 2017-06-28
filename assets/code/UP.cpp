© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

/* ARRAYQUEUE IMPLEMENTATION (SAMPLE CODE) */
#ifndef _ARRAYQUEUE_CPP
#define _ARRAYQUEUE_CPP

#include "ArrayQueue.hpp"
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;

ArrayQueue::ArrayQueue()
{
    head = 0;
    tail = 0;
    capacity = 100000;
    array = new PuzzleState * [capacity];
}
void ArrayQueue::add(PuzzleState *elem)
{
    ensure_capacity(size);
    array[tail] = elem;
    tail = (tail + 1) % capacity;
    size ++;
}

PuzzleState *ArrayQueue::remove()
{
    PuzzleState * r = array[head];
    head = (head +1) % capacity;
    size --;
    return r;
}

bool ArrayQueue::is_empty()
{
    return size == 0;
}


void ArrayQueue::ensure_capacity(int n)
{
    if(n > capacity){
      if (!is_empty()) {
      int target_capacity = (n > 2 * capacity + 1) ? n : (2 * capacity + 1);

      PuzzleState ** oldArray = array;
      array = new PuzzleState * [target_capacity];
      
      for(int i =0; i<size; i++){
          array[i] = oldArray[(head+i) % size];
      }
      
      head = 0;
      tail = size;
      capacity = target_capacity;
      delete [] oldArray;
  }
    }
}


ArrayQueue::~ArrayQueue()
{
    delete [] array;
}

#endif