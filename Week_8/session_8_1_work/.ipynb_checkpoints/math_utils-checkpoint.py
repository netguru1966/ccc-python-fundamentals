{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0897f4dc-eb0f-4c0b-98ae-7b75c9b9b186",
   "metadata": {},
   "source": [
    "## Creating Your First Module"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e0319f71-5d77-4513-8cc2-352a8dfea841",
   "metadata": {},
   "outputs": [],
   "source": [
    "# File: math_utils.py\n",
    "\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "\n",
    "def multiply(a, b):\n",
    "    return a * b\n",
    "\n",
    "def calculate_average(numbers):\n",
    "    return sum(numbers) / len(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "12fb7314-659d-4e3b-a246-6dd452a07b15",
   "metadata": {},
   "outputs": [],
   "source": [
    "PI = 3.14159"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e2cd4b3b-2e92-4a86-b287-ca89594ec254",
   "metadata": {},
   "outputs": [],
   "source": [
    "# That's it! This is a module\n",
    "# Save as math_utils.py\n",
    "# Now any file can import and use these functions!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8bd3f90a-fb7a-45eb-8d3a-d7af317d42a8",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'math_utils'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[11], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmath_utils\u001b[39;00m\n\u001b[1;32m      3\u001b[0m math_utils\u001b[38;5;241m.\u001b[39madd(\u001b[38;5;241m5\u001b[39m,\u001b[38;5;241m3\u001b[39m)\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'math_utils'"
     ]
    }
   ],
   "source": [
    "import math_utils\n",
    "\n",
    "math_utils.add(5,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd4caaa7-06a8-44f5-95db-75d21b5c17ae",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
