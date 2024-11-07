import cv2 as cv


class Triangle:
    __point_a_x: float
    __point_a_y: float

    __point_b_x: float
    __point_b_y: float

    __point_c_x: float
    __point_c_y: float

    def __init__(
        self,
        a_x: float,
        a_y: float,

        b_x: float,
        b_y: float,

        c_x: float,
        c_y: float,
    ):
        __PRECISION_SCALING: float = 1_000
        self.__point_a_x = a_x * __PRECISION_SCALING
        self.__point_a_y = a_y * __PRECISION_SCALING
        self.__point_b_x = b_x * __PRECISION_SCALING
        self.__point_b_y = b_y * __PRECISION_SCALING
        self.__point_c_x = c_x * __PRECISION_SCALING
        self.__point_c_y = c_y * __PRECISION_SCALING

    def get_area(self) -> float:
        return abs(0.5 * (
            self.__point_a_x * (self.__point_b_y - self.__point_c_y) +
            self.__point_b_x * (self.__point_c_y - self.__point_a_y) +
            self.__point_c_x * (self.__point_a_y - self.__point_b_y)
        ))

    def get_x(self) -> float:
        return self.__point_a_x

    def get_y(self) -> float:
        return self.__point_a_y

    def draw(self, frame: cv.Mat) -> cv.Mat:
        height, width, _ = frame.shape

        draw_image = cv.line(
            frame.copy(),
            (
                int(self.__point_a_x * width),
                int(self.__point_a_y * height),
            ),
            (
                int(self.__point_b_x * width),
                int(self.__point_b_y * height),
            ),
            (255, 0, 0),
            1
        )

        draw_image = cv.line(
            draw_image,
            (
                int(self.__point_a_x * width),
                int(self.__point_a_y * height),
            ),
            (
                int(self.__point_c_x * width),
                int(self.__point_c_y * height),
            ),
            (255, 0, 0),
            1
        )

        draw_image = cv.line(
            draw_image,
            (
                int(self.__point_c_x * width),
                int(self.__point_c_y * height),
            ),
            (
                int(self.__point_b_x * width),
                int(self.__point_b_y * height),
            ),
            (255, 0, 0),
            1
        )

        draw_image = cv.circle(
            draw_image,
            (
                int(self.__point_a_x * width),
                int(self.__point_a_y * height)
            ),
            4,
            (255, 0, 0),
            -1
        )

        draw_image = cv.circle(
            draw_image,
            (
                int(self.__point_b_x * width),
                int(self.__point_b_y * height)
            ),
            4,
            (0, 255, 0),
            -1
        )

        draw_image = cv.circle(
            draw_image,
            (
                int(self.__point_c_x * width),
                int(self.__point_c_y * height)
            ),
            4,
            (0, 0, 255),
            -1
        )

        return draw_image