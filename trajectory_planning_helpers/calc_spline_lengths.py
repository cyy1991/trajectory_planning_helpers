import numpy as np


def calc_spline_lengths(coeffs_x: np.ndarray, coeffs_y: np.ndarray, quickndirty: bool = False,
                        no_interp_points: int = 15) -> np.ndarray:
    """
    Created by:
    Alexander Heilmeier

    Documentation: Calculate spline lengths for third order splines defining x- and y-coordinates by usage of
    intermediate steps.

    Inputs:
    coeffs_x: coefficient matrix of the x splines with size no_splines x 4.
    coeffs_y: coefficient matrix of the y splines with size no_splines x 4.
    quickndirty: flag returns lengths based on distance between first and last spline point.
    no_interp_points: length calculation is carried out with the given number of interpolation steps.
    """

    # ------------------------------------------------------------------------------------------------------------------
    # PREPARATIONS -----------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # catch case with only one spline
    if coeffs_x.size == 4 and coeffs_x.shape[0] == 4:
        coeffs_x = np.expand_dims(coeffs_x, 0)
        coeffs_y = np.expand_dims(coeffs_y, 0)

    # get number of splines and create output array
    no_splines = coeffs_x.shape[0]
    spline_lengths = np.zeros(no_splines)

    # ------------------------------------------------------------------------------------------------------------------
    # CALCULATE LENGHTS ------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    if quickndirty:
        for i in range(no_splines):
            spline_lengths[i] = np.sqrt(np.power(np.sum(coeffs_x[i]) - coeffs_x[i, 0], 2)
                                        + np.power(np.sum(coeffs_y[i]) - coeffs_y[i, 0], 2))

    else:
        # loop through all the splines and calculate intermediate coordinates
        t_steps = np.linspace(0.0, 1.0, no_interp_points)
        spl_coords = np.zeros((no_interp_points, 2))

        for i in range(no_splines):
            spl_coords[:, 0] = coeffs_x[i, 0] \
                               + coeffs_x[i, 1] * t_steps \
                               + coeffs_x[i, 2] * np.power(t_steps, 2) \
                               + coeffs_x[i, 3] * np.power(t_steps, 3)
            spl_coords[:, 1] = coeffs_y[i, 0] \
                               + coeffs_y[i, 1] * t_steps \
                               + coeffs_y[i, 2] * np.power(t_steps, 2) \
                               + coeffs_y[i, 3] * np.power(t_steps, 3)

            spline_lengths[i] = np.sum(np.sqrt(np.sum(np.power(np.diff(spl_coords, axis=0), 2), axis=1)))

    return spline_lengths


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
