{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e4f0cb7c-9650-41c7-887e-4f16abeada6d",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'utilities'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mutilities\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mstring_utils\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m low,upp\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mutilities\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmath_utils\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m square,cube\n\u001b[32m      3\u001b[39m \u001b[38;5;28mprint\u001b[39m(low(\u001b[33m\"\u001b[39m\u001b[33mHI\u001b[39m\u001b[33m\"\u001b[39m))\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'utilities'"
     ]
    }
   ],
   "source": [
    "from utilities.string_utils import low,upp\n",
    "from utilities.math_utils import square,cube\n",
    "print(low(\"HI\"))\n",
    "print(upp(\"abc\"))\n",
    "print(square(5))\n",
    "print(cube(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "233af950-7353-4950-9122-56f3f9d2c5f3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
