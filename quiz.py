'''
    请修改下段代码

    请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
    使main函数可正确运行
    输出屏幕分辨率乘积 为 1310720

'''


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


def main():
    s = Screen()
    s.width = 1280
    s.height = 1024
    print(s.resolution)


if __name__ == '__main__':
    main()
