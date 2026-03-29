class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for car in cars:
            if not stack:
                stack.append(car)
            else:
                car_ahead = stack[-1]

                car_ahead_time = (target - car_ahead[0]) / car_ahead[1]
                car_curr_time = (target - car[0]) / car[1]

                if car_curr_time > car_ahead_time:
                    stack.append(car)

        return len(stack)
