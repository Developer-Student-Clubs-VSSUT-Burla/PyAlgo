def largest_sum_subarray(size,arr):
  max_subarr = 0
  sum_of_subarr = 0
  for i in range(size):
    sum_of_subarr += arr[i]
    if sum_of_subarr < 0:
      sum_of_subarr = 0
    elif max_subarr < sum_of_subarr:
      max_subarr = sum_of_subarr
  return max_subarr