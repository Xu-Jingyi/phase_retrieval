# -*- coding:utf-8 -*-
"""
@author:Xu Jingyi
@file:SearchingDirection.py
@time:2018/11/914:37
"""
import numpy as np
import math


class LossFunction(object):

    def __init__(self, A, y, z):
        self.A = A
        self.y = y
        self.z = z

    def f(self, x_hat):
        loss = np.mean((self.z - self.A.dot(x_hat)) ** 2) / 2
        return loss

    def gradient(self, x_hat):
        z_hat = self.A.dot(x_hat) ** 2
        func = lambda i: np.dot(self.A[i].reshape(-1, 1), self.A[i].reshape(1, -1))
        grad = 2 * (z_hat - self.z) * np.dot(np.mean([func(i) for i in range(len(self.A))], axis=0), u)
        return grad


class ChooseStep(object):

    def __init__(self, loss_func, t0=1, alpha=0.3, beta=0.8):
        self.alpha = alpha
        self.beta = beta

        self.loss_func = loss_func
        self.step = t0

        self.x_hat = loss_func.x_hat


class BacktrackingLineSearch(ChooseStep):

    def __init__(self, loss_func,  t0=1, alpha=0.3, beta=0.8):
        ChooseStep.__init__(self, loss_func,  t0, alpha, beta)

    def choose_step(self):
        step = self.step
        while self.loss_func.f(self.x_hat + step * self.delta_x) >= (
                self.loss_func.f(self.x_hat) + self.alpha * step * np.dot(self.loss_func.grad.transpose(),
                                                                          self.delta_x)):
            step = step * self.beta
        return step


class StepDecline(ChooseStep):

    def __init__(self, loss_func,  t0=1, alpha=0.3, beta=0.8):
        ChooseStep.__init__(self, loss_func,  t0, alpha, beta)

    def choose_step(self):
        return min(0.1, (1 - math.exp(-1 * self.iter / 330)) / 2)


class GradientDescent(LossFunction):

    def __init__(self, A, y, z, step_chooser):
        LossFunction.__init__(self, A, y, z)
        self.delta_x = -1 * self.grad
        self.step_chooser = step_chooser

    def searching(self, x_hat, step):
        step = self.step_chooser.choose_step()
        x_new = self.x_hat + step * self.delta_x
        return x_new


class Newton(LossFunction):

    def searching(self):
        pass


class GuassianNewton(LossFunction):

    def searching(self):
        pass


class SteepestDescent(LossFunction):

    def searching(self):
        pass


class CoordinateDescent(LossFunction):

    def searching(self):
        pass
