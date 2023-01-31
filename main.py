from numericalMethods import NumericalMethod

if __name__ == '__main__':
    NM = NumericalMethod(0, 2, 0.01)
    print(f"Dichotomy method result: {NM.dehotomia()}\n"
          f"Hitoring method result: {NM.iteration()}")