{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "345\n",
      "x=345\n"
     ]
    }
   ],
   "source": [
    "x = 345\n",
    "print(f\"{x}\")\n",
    "print(f\"{x=}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "math.floor(x + y)=385\n"
     ]
    }
   ],
   "source": [
    "y = 40\n",
    "print(f\"{math.floor(x + y)=}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "theta=30  cos(radians(theta))=0.866\n"
     ]
    }
   ],
   "source": [
    "from math import cos,radians\n",
    "theta=30\n",
    "print(f'{theta=}  {cos(radians(theta))=:.3f}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'username = Marcus Bilbao length_membership.days =12,793'"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "length_membership = date.today() - member_since\n",
    "f'{username = !s} {length_membership.days =:,d}'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
