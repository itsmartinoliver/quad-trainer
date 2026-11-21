import numpy as np
from numpy.typing import NDArray

import math
import random

def random_angular_velocity(max_speed=1.0):
    """Return (wx, wy, wz), uniformly distributed in a speed ball.

    Units are whatever you choose, commonly radians per second.
    """
    z = random.uniform(-1.0, 1.0)
    azimuth = random.uniform(0.0, 2.0 * math.pi)
    radius = max_speed * random.random() ** (1.0 / 3.0)

    xy = math.sqrt(1.0 - z * z)
    return (
        radius * xy * math.cos(azimuth),
        radius * xy * math.sin(azimuth),
        radius * z,
    )

def random_quaternion():
    """Return a uniformly random unit quaternion as (w, x, y, z)."""
    q = [random.gauss(0.0, 1.0) for _ in range(4)]
    norm = math.sqrt(sum(v * v for v in q))
    return tuple(v / norm for v in q)

def quaternion_to_euler(q: NDArray) -> tuple[float, float, float]:
    w, qx, qy, qz = q
    phi = np.arctan2(2 * (w * qx + qy * qz), 1 - 2 * (qx**2 + qy**2))
    theta = np.arcsin(2 * (w * qy - qz * qx))
    psi = np.arctan2(2 * (w * qz + qx * qy), 1 - 2 * (qy**2 + qz**2))
    return float(phi), float(theta), float(psi)

def rot_vec_by_quat(q: NDArray, v: NDArray) -> NDArray:
    w = q[0]
    q_vec = q[1:4]
    t = 2.0 * np.cross(q_vec, v)
    return v + w * t + np.cross(q_vec, t)

def quat_mul(p: NDArray[np.float64], q: NDArray[np.float64]) -> NDArray[np.float64]:
    pw, px, py, pz = p
    qw, qx, qy, qz = q

    r = np.empty(4, dtype=np.float64)

    r[0] = pw * qw - px * qx - py * qy - pz * qz
    r[1] = pw * qx + px * qw + py * qz - pz * qy
    r[2] = pw * qy - px * qz + py * qw + pz * qx
    r[3] = pw * qz + px * qy - py * qx + pz * qw

    return r
