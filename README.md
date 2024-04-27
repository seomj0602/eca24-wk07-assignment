`probability_below()` 함수를 구현하시오<br>Implement `probability_below()` function.

* 매개변수는 `Vector` 형 `x_data` 와 `float` 형 `bound`<br>Arguments are `x_data` in `Vector` and `bound` in `float`.
* `x_data` 가운데 임의로 하나를 선택했을 때 `bound` 보다 작을 확률을 계산하시오<br>Calculate probability that random pick from `x_data` would be smaller than the `bound`.

``` python
>>> data = (0, 1, 2, 3, 4)
>>> bound = 1.5
>>> print(probability_below(data, bound))
0.2
```
