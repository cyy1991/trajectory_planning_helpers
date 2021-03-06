import numpy as np
import trajectory_planning_helpers.normalize_psi


def calc_head_curv_an(coeffs_x: np.ndarray, coeffs_y: np.ndarray, ind_spls: np.ndarray, t_spls: np.ndarray) -> tuple:
    """
    Created by:
    Alexander Heilmeier

    Documentation:
    Analytical calculation of heading psi and curvature kappa on the basis of third order splines for x- and
    y-coordinate.

    Inputs:
    coeffs_x: coefficient matrix of the x splines with size no_splines x 4.
    coeffs_y: coefficient matrix of the y splines with size no_splines x 4.
    ind_spls: contains the indices of the splines that hold the points for which we want to calculate heading/curvature.
    t_spls: containts the relative spline coordinate values (t) of every point on the splines.
    """

    # calculate required derivatives
    x_d = coeffs_x[ind_spls, 1] \
          + 2 * coeffs_x[ind_spls, 2] * t_spls \
          + 3 * coeffs_x[ind_spls, 3] * np.power(t_spls, 2)

    x_dd = 2 * coeffs_x[ind_spls, 2] \
           + 6 * coeffs_x[ind_spls, 3] * t_spls

    y_d = coeffs_y[ind_spls, 1] \
          + 2 * coeffs_y[ind_spls, 2] * t_spls \
          + 3 * coeffs_y[ind_spls, 3] * np.power(t_spls, 2)

    y_dd = 2 * coeffs_y[ind_spls, 2] \
           + 6 * coeffs_y[ind_spls, 3] * t_spls

    # calculate heading psi (pi/2 must be substracted due to our convention that psi = 0 is north)
    psi = np.arctan2(y_d, x_d) - np.pi / 2
    psi = trajectory_planning_helpers.normalize_psi.normalize_psi(psi)

    # calculate curvature kappa
    kappa = (x_d * y_dd - y_d * x_dd) / np.power(np.power(x_d, 2) + np.power(y_d, 2), 1.5)

    return psi, kappa


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
