class two_d_vector:
    x_axis = 0
    y_axix = 0
    def two_d(self):
        print(f"The coordinates are : {self.x_axis}i+{self.y_axix}j ")
class three_D_vector(two_d_vector):
    z_axis = 0
    def three_D(self):
        print(f"The coordinates are : {self.x_axis}i + {self.y_axix}j + {self.z_axis}k ")

hello = three_D_vector()
hello.x_axis=10
hello.y_axix=85
hello.z_axis=85
hello.three_D()