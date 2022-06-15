#  Python package `ishihara-like-mnist`
#
#  file: plates.py
#
#  Authors: Ammar Shaker  (Ammar.Shaker@neclab.eu)
#
#  NEC Laboratories Europe GmbH, Copyright (c) 2022, All rights reserved.
#  THIS HEADER MAY NOT BE EXTRACTED OR MODIFIED IN ANY WAY.
#
#  --- PROPRIETARY INFORMATION ---
#
#  SOFTWARE LICENSE Agreement
#  ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY
#  BY USING OR DOWNLOADING THE SOFTWARE, YOU ARE AGREEING TO THE TERMS OF THIS LICENSE
#  AGREEMENT.  IF YOU DO NOT AGREE WITH THESE TERMS, YOU MAY NOT USE OR DOWNLOAD THE
#  SOFTWARE.
#
#  This is a license agreement ("Agreement") between your academic institution or
#  non-profit organization or self (called "Licensee" or "You" in this Agreement) and
#  NEC Laboratories Europe GmbH (called "Licensor" in this Agreement).  All rights not
#  specifically granted to you in this Agreement are reserved for Licensor.
#  RESERVATION OF OWNERSHIP AND GRANT OF LICENSE: Licensor retains exclusive ownership
#  of any copy of the Software (as defined below) licensed under this Agreement and
#  hereby grants to Licensee a personal, non-exclusive, non-transferable license to use
#  the Software for noncommercial research purposes, without the right to sublicense,
#  pursuant to the terms and conditions of this Agreement. NO EXPRESS OR IMPLIED
#  LICENSES TO ANY OF LICENSOR’S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. As used in
#  this Agreement, the term "Software" means (i) the actual copy of all or any portion
#  of code for program routines made accessible to Licensee by Licensor pursuant to
#  this Agreement, inclusive of backups, updates, and/or merged copies permitted
#  hereunder or subsequently supplied by Licensor,  including all or any file
#  structures, programming instructions, user interfaces and screen formats and
#  sequences as well as any and all documentation and instructions related to it,
#  and (ii) all or any derivatives and/or modifications created or made by You to any
#  of the items specified in (i).
#  CONFIDENTIALITY/PUBLICATIONS: Licensee acknowledges that the Software is proprietary
#  to Licensor, and as such, Licensee agrees to receive all such materials and to use
#  the Software only in accordance with the terms of this Agreement.  Licensee agrees
#  to use reasonable effort to protect the Software from unauthorized use,
#  reproduction, distribution, or publication. All publication materials mentioning
#  features or use of this software must explicitly include an acknowledgement the
#  software was developed by NEC Laboratories Europe GmbH.
#  COPYRIGHT: The Software is owned by Licensor.
#  PERMITTED USES:  The Software may be used for your own noncommercial internal
#  research purposes. You understand and agree that Licensor is not obligated to
#  implement any suggestions and/or feedback you might provide regarding the Software,
#  but to the extent Licensor does so, you are not entitled to any compensation related
#  thereto.
#  DERIVATIVES: You may create derivatives of or make modifications to the Software,
#  however, You agree that all and any such derivatives and modifications will be
#  owned by Licensor and become a part of the Software licensed to You under this
#  Agreement.  You may only use such derivatives and modifications for your own
#  noncommercial internal research purposes, and you may not otherwise use, distribute
#  or copy such derivatives and modifications in violation of this Agreement.
#  BACKUPS:  If Licensee is an organization, it may make that number of copies of the
#  Software necessary for internal noncommercial use at a single site within its
#  organization provided that all information appearing in or on the original labels,
#  including the copyright and trademark notices are copied onto the labels of the
#  copies.
#  USES NOT PERMITTED:  You may not distribute, copy or use the Software except as
#  explicitly permitted herein. Licensee has not been granted any trademark license as
#  part of this Agreement. Neither the name of NEC Laboratories Europe GmbH nor the
#  names of its contributors may be used to endorse or promote products derived from
#  this Software without specific prior written permission.
#  You may not sell, rent, lease, sublicense, lend, time-share or transfer, in whole or
#  in part, or provide third parties access to prior or present versions (or any parts
#  thereof) of the Software.
#  ASSIGNMENT: You may not assign this Agreement or your rights hereunder without the
#  prior written consent of Licensor. Any attempted assignment without such consent
#  shall be null and void.
#  TERM: The term of the license granted by this Agreement is from Licensee's
#  acceptance of this Agreement by downloading the Software or by using the Software
#  until terminated as provided below.
#  The Agreement automatically terminates without notice if you fail to comply with any
#  provision of this Agreement.  Licensee may terminate this Agreement by ceasing using
#  the Software.  Upon any termination of this Agreement, Licensee will delete any and
#  all copies of the Software. You agree that all provisions which operate to protect
#  the proprietary rights of Licensor shall remain in force should breach occur and
#  that the obligation of confidentiality described in this Agreement is binding in
#  perpetuity and, as such, survives the term of the Agreement.
#  FEE: Provided Licensee abides completely by the terms and conditions of this
#  Agreement, there is no fee due to Licensor for Licensee's use of the Software in
#  accordance with this Agreement.
#  DISCLAIMER OF WARRANTIES:  THE SOFTWARE IS PROVIDED "AS-IS" WITHOUT WARRANTY OF ANY
#  KIND INCLUDING ANY WARRANTIES OF PERFORMANCE OR MERCHANTABILITY OR FITNESS FOR A
#  PARTICULAR USE OR PURPOSE OR OF NON-INFRINGEMENT.  LICENSEE BEARS ALL RISK RELATING
#  TO QUALITY AND PERFORMANCE OF THE SOFTWARE AND RELATED MATERIALS.
#  SUPPORT AND MAINTENANCE: No Software support or training by the Licensor is provided
#  as part of this Agreement.
#  EXCLUSIVE REMEDY AND LIMITATION OF LIABILITY: To the maximum extent permitted under
#  applicable law, Licensor shall not be liable for direct, indirect, special,
#  incidental, or consequential damages or lost profits related to Licensee's use of
#  and/or inability to use the Software, even if Licensor is advised of the possibility
#  of such damage.
#  EXPORT REGULATION: Licensee agrees to comply with any and all applicable export
#  control laws, regulations, and/or other laws related to embargoes and sanction
#  programs administered by law.
#  SEVERABILITY: If any provision(s) of this Agreement shall be held to be invalid,
#  illegal, or unenforceable by a court or other tribunal of competent jurisdiction,
#  the validity, legality and enforceability of the remaining provisions shall not in
#  any way be affected or impaired thereby.
#  NO IMPLIED WAIVERS: No failure or delay by Licensor in enforcing any right or remedy
#  under this Agreement shall be construed as a waiver of any future or other exercise
#  of such right or remedy by Licensor.
#  GOVERNING LAW: This Agreement shall be construed and enforced in accordance with the
#  laws of Germany without reference to conflict of laws principles.  You consent to the
#  personal jurisdiction of the courts of this country and waive their rights to venue
#  outside of Germany.
#  ENTIRE AGREEMENT AND AMENDMENTS: This Agreement constitutes the sole and entire
#  agreement between Licensee and Licensor as to the matter set forth herein and
#  supersedes any previous agreements, understandings, and arrangements between
#  the parties relating hereto.
#      THIS HEADER MAY NOT BE EXTRACTED OR MODIFIED IN ANY WAY.
"""
   This module contains helping functions for the plotting of the differet Ishihara
   plates.
"""
import math
import os
import pickle
import secrets
import shutil
from os.path import exists, join
from pathlib import Path
from typing import Callable, Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from sklearn.cluster import KMeans

from IshiharaMC import ishiharaMC

# This dictionary contains the extracted colors and their distributions from Ishihara's
# book, besides different functions for the plate creation.
Plates_Dict = {
    1: {
        "foreground": {"NormalColors": [("#f45f26", 121870)]},
        "background": {"NormalColors": [("#858f84", 660716)]},
    },
    2: {
        "foreground": {
            "NormalColors": [("#d47773", 56956), ("#dd9c80", 85806)],
            "SpecialColors": [("#c36833", 8172), ("#e99c69", 20111)],
            "Note": "Special colors should be in the left most part",
        },
        "background": {
            "NormalColors": [("#927f36", 199516), ("#bda356", 279799), ("#bda356", 0)],
            "SpecialColors": [("#8c8c56", 38553), ("#c4bd79", 200327)],
            "Note": "Special colors should be in the left most part and close to the "
            "special foreground colors",
        },
    },
    3: {
        "foreground": {
            "NormalColors": [("#d0736d", 59380), ("#db9980", 62291)],
            "SpecialColors": [("#c66a34", 19231), ("#e4915f", 25411)],
            "n_clusters": 20,
            "perc_clusters": 0.5,
            "Note": "Special colors should be in clusters",
        },
        "background": {
            "NormalColors": [
                ("#88752e", 244713),
                ("#af9448", 160367),
                ("#c9af63", 179615),
            ],
            "SpecialColors": [("#878756", 40062), ("#cec188", 180927)],
            "Note": "Special colors should be in the left most part and close to the "
            "special foreground colors",
        },
    },
    4: {
        "foreground": {
            "NormalColors": [("#7c8b62", 23603), ("#bec081", 30742)],
            "SpecialColors": [
                ("#927928", 25326),
                ("#b89f4e", 26187),
                ("#cfb663", 28348),
            ],
            "n_clusters": 10,
            "perc_clusters": 0.5,
            "Note": "Special colors should be in clusters",
        },
        "background": {
            "NormalColors": [
                ("#c7512b", 206337),
                ("#e57e52", 236899),
                ("#f69f78", 98095),
            ],
            "SpecialColors": [("#b3504c", 67062), ("#da9880", 109247)],
            "Note": "Special colors should be in the center most part and close "
            "to the centered foreground",
        },
    },
    5: {
        "foreground": {
            "NormalColors": [("#808f64", 46115), ("#a6aa6c", 30569)],
            "SpecialColors": [
                ("#947b2a", 17175),
                ("#b49a4a", 20000),
                ("#cfb663", 12057),
            ],
            "n_clusters": 7,
            "perc_clusters": 0.7,
            "Note": "Special colors should be in clusters. Clusters should be only in "
            "the upper part.",
        },
        "background": {
            "NormalColors": [
                ("#c8532b", 259328),
                ("#db7549", 143369),
                ("#ed9d75", 190926),
            ],
            "SpecialColors": [("#a74541", 41553), ("#e1a088", 137079)],
            "Note": "Special colors should be in the upper most part and close to the "
            "special foreground colors",
        },
    },
    6: {
        "foreground": {
            "NormalColors": [("#7e8c64", 40268), ("#b7b97a", 43126)],
            "SpecialColors": [
                ("#957e28", 20843),
                ("#b3994b", 22620),
                ("#d1b964", 22648),
            ],
            "n_clusters": 7,
            "perc_clusters": 0.7,
            "Note": "Special colors should be in right lower most part",
        },
        "background": {
            "NormalColors": [
                ("#c6502a", 187518),
                ("#ea7e4d", 183887),
                ("#f69e77", 144248),
            ],
            "SpecialColors": [("#b14f4c", 50756), ("#dd9b83", 157207)],
            "Note": "Special colors should be in the right most close to the special "
            "foreground colors",
        },
    },
    7: {
        "foreground": {
            "NormalColors": [("#7e8d63", 59151), ("#bbbd7f", 61368)],
            "SpecialColors": [
                ("#927a2d", 29739),
                ("#b79d4f", 29875),
                ("#cab460", 19109),
            ],
            "n_clusters": 10,
            "perc_clusters": 0.5,
            "Note": "Special colors should be in clusters",
        },
        "background": {
            "NormalColors": [
                ("#c6502a", 198814),
                ("#e57f53", 227099),
                ("#fba47c", 85980),
            ],
            "SpecialColors": [("#b04d49", 60581), ("#db9981", 113219)],
            "Note": "Special colors should be in the left most part and close to the "
            "special foreground colors",
        },
    },
    8: {
        "foreground": {
            "NormalColors": [
                ("#c25d31", 32571),
                ("#dc7e51", 44462),
                ("#ec9d72", 41145),
            ],
            "Note": "No special colors for the foreground",
        },
        "background": {
            "NormalColors": [
                ("#826529", 192828),
                ("#a78c49", 152503),
                ("#ccb06c", 190231),
                ("#87917e", 111068),
                ("#b7ac8a", 141262),
            ],
            "Note": "No special colors for the background",
        },
    },
    9: {
        "foreground": {
            "NormalColors": [
                ("#c56034", 39969),
                ("#e18557", 55325),
                ("#efa075", 63750),
            ],
            "Note": "No special colors for the foreground",
        },
        "background": {
            "NormalColors": [
                ("#80632b", 197181),
                ("#9d823f", 107735),
                ("#caaf6a", 176493),
                ("#b7ad8a", 165915),
                ("#858e7b", 63326),
            ],
            "Note": "No special colors for the background",
        },
    },
    10: {
        "foreground": {
            "NormalColors": [
                ("#647439", 24489),
                ("#87985c", 30662),
                ("#afb26b", 49437),
            ],
            "Note": "No special colors for the foreground",
        },
        "background": {
            "NormalColors": [
                ("#aa342a", 200379),
                ("#e06661", 162349),
                ("#f99e8f", 309442),
                ("#ed8c16", 83991),
                ("#f8b412", 47114),
            ],
            "Note": "No special colors for the background",
        },
    },
    11: {
        "foreground": {
            "NormalColors": [
                ("#707a3e", 22448),
                ("#88975c", 23124),
                ("#a9ac66", 40309),
            ],
            "Note": "No special colors for the foreground",
        },
        "background": {
            "NormalColors": [
                ("#ae362b", 174224),
                ("#e26861", 146455),
                ("#f59687", 281983),
                ("#ef8d15", 102401),
                ("#f8b511", 71260),
            ],
            "Note": "No special colors for the background",
        },
    },
    12: {
        "foreground": {
            "NormalColors": [
                ("#708242", 59976),
                ("#87985c", 29307),
                ("#b2b670", 54123),
            ],
            "Note": "No special colors for the foreground",
        },
        "background": {
            "NormalColors": [
                ("#b2392d", 184243),
                ("#ec726d", 174660),
                ("#fa9f90", 264217),
                ("#f09616", 56273),
                ("#fcba18", 69272),
            ],
            "Note": "No special colors for the background",
        },
    },
    13: {
        "foreground": {
            "NormalColors": [
                ("#697439", 38764),
                ("#86975c", 41565),
                ("#a6aa66", 60382),
            ],
            "Note": "No special colors for the foreground",
        },
        "background": {
            "NormalColors": [
                ("#a52f25", 172928),
                ("#de635e", 152931),
                ("#f29183", 243408),
                ("#f08f17", 78301),
                ("#f9b515", 78125),
            ],
            "Note": "No special colors for the background",
        },
    },
    16: {
        "foreground": {
            "NormalColors": [("#da3124", 29134), ("#f4585c", 31690)],
            "SpecialColors": [
                ("#922940", 32308),
                ("#ce6075", 35069),
                ("#dd8689", 82240),
            ],
            "Note": "Special colors on the right part of the figure",
        },
        "background": {
            "NormalColors": [
                ("#3a2927", 197696),
                ("#6e5656", 170538),
                ("#a58e7e", 261258),
            ],
            "Note": "No special colors for the background",
        },
    },
    17: {
        "foreground": {
            "NormalColors": [("#d92c1c", 30298), ("#f5797c", 22877)],
            "SpecialColors": [
                ("#912942", 29398),
                ("#c95a70", 40061),
                ("#dd8086", 92498),
            ],
            "Note": "Special colors on the right part of the figure",
        },
        "background": {
            "NormalColors": [
                ("#362623", 220170),
                ("#6a5252", 200830),
                ("#967f77", 250247),
            ],
            "Note": "No special colors for the background",
        },
    },
    20: {"color_fg": "k", "color_bg": "k"},
    21: {
        "color_fg": "k",
        "color_bg": "k",
        "num_random_points_fg": 0,
        "num_random_points_bg": 0,
        "connected_fg": False,
        "connected_bg": False,
    },
}


def load_pkl(pickle_file: str) -> Tuple[np.ndarray, np.ndarray]:
    """This function reads a pickle file and returns a list of circles and indicators.
    Each circle has an indicator of whether a circle is in the target digit or not.
    """

    with open(pickle_file, "rb") as file:
        data = pickle.load(file)
    return data["output"], data["idx_final"]


def plotpoints(
    circles: np.ndarray,
    num_random_points: int = 0,
    color: str = None,
    connected: bool = False,
) -> None:
    """This function takes a list of circles, a number of dots, their color, and
    whether or not the dots should be connected.
    The function reduces each circle into a dot and plots a number of dots on its
    circumference, depending on the configurations.
    """

    plt.gca()
    if color is None:
        color = "k"
    plt.scatter(circles[:, 0], circles[:, 1], marker=".", s=10, color=color)
    if num_random_points > 0:
        random_angels = np.random.uniform(
            low=0.0, high=360, size=(circles.shape[0], num_random_points)
        )
        x_random = circles[:, 0:1] + np.cos(random_angels) * circles[:, 2:]
        y_random = circles[:, 1:2] + np.sin(random_angels) * circles[:, 2:]
        if connected:
            for ind, i in enumerate(circles):
                plt.plot(x_random[ind, :], y_random[ind, :], ms=10, color=color)
        else:
            plt.scatter(x_random, y_random, s=10, color=color)
    plt.axis([-1, 1, -1, 1])
    plt.gca().set_aspect("equal")


def create_folder_tree(path: str, name: str, first_level_only: bool = False) -> None:
    """This function creates the necessary folder structure needed for a new plate."""
    Path(join(path, name, "Test_images")).mkdir(parents=True, exist_ok=True)
    Path(join(path, name, "Train_images")).mkdir(parents=True, exist_ok=True)
    if not first_level_only:
        for i in range(10):
            Path(join(path, name, "Test_images", str(i))).mkdir(
                parents=True, exist_ok=True
            )
            Path(join(path, name, "Train_images", str(i))).mkdir(
                parents=True, exist_ok=True
            )


def get_sample(colors_histo: List[Tuple], sample_size: int) -> np.ndarray:
    """This function takes a list of colors, their histogram, and the number of points
    to be sampled.
    Depending on the histogram, the function samples the number of circles for each
    color according to the multinomial distribution.
    """
    prob = [x[1] for x in colors_histo]
    prob = [x / sum(prob) for x in prob]
    sample = np.random.multinomial(1, prob, size=sample_size)
    return sample


def compute_clusters(data: np.ndarray, n_clusters: int) -> KMeans:
    """This function takes a list of circles and applies KMeans clustering on them."""
    n_clusters = min(n_clusters, data.shape[0])
    kmeans = KMeans(
        init="random", n_clusters=n_clusters, n_init=10, max_iter=100, random_state=42
    )
    kmeans.fit(data)
    return kmeans


def plot_circles(circles: np.ndarray, colors: List[Tuple]) -> None:
    """This function takes a list of circles and colors. According to the colors'
    histograms, it distributes the colors over the circles."""
    sample = get_sample(colors, circles.shape[0])
    for i, c in enumerate(colors):
        indnew = sample[:, i] == 1
        ishiharaMC.plotIshi(circles[indnew], color=c[0])


def sort_background_according_special_foreground(
    foreground: np.ndarray,
    background: np.ndarray,
    center_foreground: np.ndarray,
    percent_foreground: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """This function takes the foreground, the background, and the point of interest
    and returns a sorted list of the special foreground and background."""
    special_foreground = math.ceil(percent_foreground * (foreground.shape[0]))

    distances = np.apply_along_axis(
        np.linalg.norm, 1, foreground[:, :2] - center_foreground
    )
    foreground_sorted = np.argsort(distances)
    chosen_left_foreground_ind = foreground_sorted[:special_foreground]
    chosen_left_foreground = foreground[chosen_left_foreground_ind, :]

    background_sorted = np.argsort(
        [
            np.apply_along_axis(
                np.linalg.norm, 1, chosen_left_foreground[:, :2] - x
            ).min()
            for x in background[:, :2]
        ]
    )
    return foreground_sorted, background_sorted


def plot_plate_generic(
    output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict
) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a generic Ishihara plate, e.g., plates 1, 8-13
    """

    foreground_colors = Plate_Dic["foreground"]["NormalColors"]
    background_colors = Plate_Dic["background"]["NormalColors"]

    foreground, background = output[idx_final], output[np.logical_not(idx_final)]

    plot_circles(background, background_colors)
    plot_circles(foreground, foreground_colors)


def plot_plate2(output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a the Ishihara plate 2.
    """

    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["SpecialColors"],
        Plate_Dic["background"]["SpecialColors"],
    )

    foreground = output[idx_final]
    background = output[np.logical_not(idx_final)]
    percent_special_foreground, percent_special_background = 0.2, 0.05
    special_foreground, special_background = (
        math.ceil(percent_special_foreground * (foreground.shape[0])),
        math.ceil(percent_special_background * (background.shape[0])),
    )

    center = np.array([-1, 0])
    foreground_sorted, background_sorted = sort_background_according_special_foreground(
        foreground, background, center, percent_special_foreground
    )
    chosen_foreground_ind = foreground_sorted[:special_foreground]
    chosen_foreground = foreground[chosen_foreground_ind, :]
    plot_circles(chosen_foreground, foreground_colors)

    chosen_background_ind = background_sorted[:special_background]
    chosen_background = background[chosen_background_ind, :]
    plot_circles(chosen_background, background_colors)

    ################################
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["NormalColors"],
        Plate_Dic["background"]["NormalColors"],
    )

    non_chosen_foreground_ind = foreground_sorted[special_foreground:]
    non_chosen_foreground = foreground[non_chosen_foreground_ind, :]
    plot_circles(non_chosen_foreground, foreground_colors)

    non_chosen_background_ind = background_sorted[special_background:]
    non_chosen_background = background[non_chosen_background_ind, :]
    plot_circles(non_chosen_background, background_colors)


def plot_plate3(output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a the Ishihara plate 3.
    """

    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["SpecialColors"],
        Plate_Dic["background"]["SpecialColors"],
    )
    foreground, background = output[idx_final], output[np.logical_not(idx_final)]

    kmeans = compute_clusters(foreground[:, :2], Plate_Dic["foreground"]["n_clusters"])
    inside = kmeans.labels_ < math.floor(
        Plate_Dic["foreground"]["n_clusters"] * Plate_Dic["foreground"]["perc_clusters"]
    )

    chosen_foreground = foreground[inside, :]
    non_chosen_foreground = foreground[np.logical_not(inside), :]
    plot_circles(chosen_foreground, foreground_colors)

    percent_special_background = 0.1
    special_background = math.ceil(percent_special_background * (background.shape[0]))

    left_most_foreground = foreground[:, 0] < 0
    threshold = 0.0
    special_foreground = math.ceil(0.2 * (foreground.shape[0]))

    while sum(left_most_foreground) < special_foreground:
        threshold += 0.001
        left_most_foreground = foreground[:, 0] < (0 + threshold)

    chosen_top_foreground = foreground[left_most_foreground, :]
    background_sorted = np.argsort(
        [
            np.apply_along_axis(
                np.linalg.norm, 1, chosen_top_foreground[:, :2] - x
            ).min()
            for x in background[:, :2]
        ]
    )

    chosen_background_ind = background_sorted[:special_background]
    chosen_background = background[chosen_background_ind, :]
    plot_circles(chosen_background, background_colors)
    ################################
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["NormalColors"],
        Plate_Dic["background"]["NormalColors"],
    )

    plot_circles(non_chosen_foreground, foreground_colors)

    non_chosen_background_ind = background_sorted[special_background:]
    non_chosen_background = background[non_chosen_background_ind, :]
    plot_circles(non_chosen_background, background_colors)


def plot_plate4(output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a the Ishihara plate 4.
    """
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["SpecialColors"],
        Plate_Dic["background"]["SpecialColors"],
    )
    foreground, background = output[idx_final], output[np.logical_not(idx_final)]

    kmeans = compute_clusters(foreground[:, :2], Plate_Dic["foreground"]["n_clusters"])
    inside = kmeans.labels_ < math.floor(
        Plate_Dic["foreground"]["n_clusters"] * Plate_Dic["foreground"]["perc_clusters"]
    )

    chosen_foreground = foreground[inside, :]
    non_chosen_foreground = foreground[np.logical_not(inside), :]
    plot_circles(chosen_foreground, foreground_colors)

    percent_special_foreground, percent_special_background = 0.35, 0.15
    special_background = math.floor(percent_special_background * (background.shape[0]))
    center = np.array([0, 0])

    foreground_sorted, background_sorted = sort_background_according_special_foreground(
        foreground, background, center, percent_special_foreground
    )

    chosen_background_ind = background_sorted[:special_background]
    chosen_background = background[chosen_background_ind, :]
    plot_circles(chosen_background, background_colors)
    ################################
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["NormalColors"],
        Plate_Dic["background"]["NormalColors"],
    )

    plot_circles(non_chosen_foreground, foreground_colors)

    non_chosen_background_ind = background_sorted[special_background:]
    non_chosen_background = background[non_chosen_background_ind, :]
    plot_circles(non_chosen_background, background_colors)


def plot_plate5(output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a the Ishihara plate 5.
    """

    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["SpecialColors"],
        Plate_Dic["background"]["SpecialColors"],
    )
    foreground, background = output[idx_final], output[np.logical_not(idx_final)]

    top_most = foreground[:, 1] > 0
    chosen_top_foreground = foreground[top_most, :]
    kmeans = compute_clusters(
        chosen_top_foreground[:, :2], Plate_Dic["foreground"]["n_clusters"]
    )
    inside = kmeans.labels_ < math.floor(
        Plate_Dic["foreground"]["n_clusters"] * Plate_Dic["foreground"]["perc_clusters"]
    )
    chosen_foreground = chosen_top_foreground[inside, :]

    plot_circles(chosen_foreground, foreground_colors)

    non_chosen_top_foreground = chosen_top_foreground[np.logical_not(inside), :]
    non_chosen_foreground = foreground[np.logical_not(top_most), :]

    percent_special_background = 0.1
    special_background = math.ceil(percent_special_background * (background.shape[0]))

    background_sorted = np.argsort(
        [
            np.apply_along_axis(
                np.linalg.norm, 1, chosen_top_foreground[:, :2] - x
            ).min()
            for x in background[:, :2]
        ]
    )

    chosen_background_ind = background_sorted[:special_background]
    chosen_background = background[chosen_background_ind, :]
    plot_circles(chosen_background, background_colors)
    ################################
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["NormalColors"],
        Plate_Dic["background"]["NormalColors"],
    )

    plot_circles(non_chosen_top_foreground, foreground_colors)
    plot_circles(non_chosen_foreground, foreground_colors)

    non_chosen_background_ind = background_sorted[special_background:]
    non_chosen_background = background[non_chosen_background_ind, :]
    plot_circles(non_chosen_background, background_colors)


def plot_plate6(output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a the Ishihara plate 6.
    """

    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["SpecialColors"],
        Plate_Dic["background"]["SpecialColors"],
    )
    foreground, background = output[idx_final], output[np.logical_not(idx_final)]

    right_lower_most = np.logical_and(foreground[:, 0] > 0, foreground[:, 1] < 0)
    threshold = 0.0
    while sum(right_lower_most) < 20:
        threshold += 0.001
        right_lower_most = np.logical_and(
            foreground[:, 0] > 0 - threshold, foreground[:, 1] < 0 + threshold
        )

    chosen_right_lower_foreground = foreground[right_lower_most, :]
    kmeans = compute_clusters(
        chosen_right_lower_foreground[:, :2], Plate_Dic["foreground"]["n_clusters"]
    )
    inside = kmeans.labels_ < math.floor(
        Plate_Dic["foreground"]["n_clusters"] * Plate_Dic["foreground"]["perc_clusters"]
    )
    chosen_foreground = chosen_right_lower_foreground[inside, :]

    plot_circles(chosen_foreground, foreground_colors)

    non_chosen_right_lower_foreground = chosen_right_lower_foreground[
        np.logical_not(inside), :
    ]
    non_chosen_foreground = foreground[np.logical_not(right_lower_most), :]

    percent_special_background = 0.1
    special_background = math.ceil(percent_special_background * (background.shape[0]))
    right_most_foreground = foreground[foreground[:, 0] > 0]
    background_sorted = np.argsort(
        [
            np.apply_along_axis(
                np.linalg.norm, 1, right_most_foreground[:, :2] - x
            ).min()
            for x in background[:, :2]
        ]
    )

    chosen_background_ind = background_sorted[:special_background]
    chosen_background = background[chosen_background_ind, :]
    plot_circles(chosen_background, background_colors)
    ################################
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["NormalColors"],
        Plate_Dic["background"]["NormalColors"],
    )

    plot_circles(non_chosen_right_lower_foreground, foreground_colors)
    plot_circles(non_chosen_foreground, foreground_colors)

    non_chosen_background_ind = background_sorted[special_background:]
    non_chosen_background = background[non_chosen_background_ind, :]
    plot_circles(non_chosen_background, background_colors)


def plot_plate7(output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a the Ishihara plate 7.
    """

    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["SpecialColors"],
        Plate_Dic["background"]["SpecialColors"],
    )
    foreground, background = output[idx_final], output[np.logical_not(idx_final)]

    kmeans = compute_clusters(foreground[:, :2], Plate_Dic["foreground"]["n_clusters"])
    inside = kmeans.labels_ < math.floor(
        Plate_Dic["foreground"]["n_clusters"] * Plate_Dic["foreground"]["perc_clusters"]
    )

    chosen_foreground = foreground[inside, :]
    non_chosen_foreground = foreground[np.logical_not(inside), :]
    plot_circles(chosen_foreground, foreground_colors)

    percent_special_background = 0.2
    special_background = math.ceil(percent_special_background * (background.shape[0]))

    left_most_foreground = foreground[:, 0] < 0
    threshold = 0.0
    special_foreground = math.ceil(0.2 * (foreground.shape[0]))
    while sum(left_most_foreground) < special_foreground:
        threshold += 0.001
        left_most_foreground = foreground[:, 0] < (0 + threshold)

    chosen_left_foreground = foreground[left_most_foreground, :]

    background_sorted = np.argsort(
        [
            np.apply_along_axis(
                np.linalg.norm, 1, chosen_left_foreground[:, :2] - x
            ).min()
            for x in background[:, :2]
        ]
    )
    chosen_background_ind = background_sorted[:special_background]
    chosen_background = background[chosen_background_ind, :]
    plot_circles(chosen_background, background_colors)
    # else:
    #    background_sorted, special_background = np.arange(background.shape[0]), 0

    ################################
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["NormalColors"],
        Plate_Dic["background"]["NormalColors"],
    )

    plot_circles(non_chosen_foreground, foreground_colors)

    non_chosen_background_ind = background_sorted[special_background:]
    non_chosen_background = background[non_chosen_background_ind, :]
    plot_circles(non_chosen_background, background_colors)


def plot_plate16_17(output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting.
    The function plots a the Ishihara plates 16 and 17.
    """

    foreground_colors = Plate_Dic["foreground"]["SpecialColors"]
    foreground, background = output[idx_final], output[np.logical_not(idx_final)]

    right_most = foreground[:, 0] > 0
    chosen_foreground = foreground[right_most, :]
    non_chosen_foreground = foreground[np.logical_not(right_most), :]
    plot_circles(chosen_foreground, foreground_colors)

    ################################
    foreground_colors, background_colors = (
        Plate_Dic["foreground"]["NormalColors"],
        Plate_Dic["background"]["NormalColors"],
    )

    plot_circles(non_chosen_foreground, foreground_colors)
    plot_circles(background, background_colors)


def create_random_plates(
    files: List[str], outpath: str, new_plate: str, suffix: str, plates: List[str]
) -> None:
    """This function created a plate by sampling images randomly from a list of plates.
    The suffix takes either "Test_images" or "Train_images".
    """
    prob = [1 / len(plates)] * len(plates)

    for f in files:
        number = f.split(os.sep)[-1].split(".")[0]
        with open(f, "rb") as file:
            data = pickle.load(file)
            random_files = np.random.multinomial(1, prob, size=len(data.keys()))
            for i, key in enumerate(data.keys()):
                ind = np.argmax(random_files[i])
                jpg_file = join(
                    outpath, plates[ind], suffix, number, key.split(".")[0] + ".jpg"
                )
                new_jpg_file = join(
                    outpath, new_plate, suffix, number, key.split(".")[0] + ".jpg"
                )
                print(jpg_file, new_jpg_file)
                shutil.copyfile(jpg_file, new_jpg_file)


def plot_plate_random_color(
    output: np.ndarray, idx_final: np.ndarray, Plate_Dic: Dict = None
) -> None:
    """This function takes a list of circles and their indicators. The dictionary here
    should remain None.
    The function assigns each circle a random color.
    """

    # pdb.set_trace()
    for circle in output:
        random_color = "#" + secrets.token_hex(3)
        ishiharaMC.plotIshi([circle], color=random_color)


def process_files(
    files: List[str],
    function: Callable,
    manipulation_function: Callable,
    path: str,
    params: Dict,
) -> None:
    """This function converts circled MNIST to Ishihara MNIST.
    It takes a list of pickle files (circled MNIST), and for each image, it calls one
    of the plate plotting functions after calling a manipulation function.
    """
    # pdb.set_trace()
    for f in files:
        number = f.split(os.sep)[-1].split(".")[0]
        with open(f, "rb") as file:
            data = pickle.load(file)

            # ------------- Shuffling the data dict
            keys = list(data.keys())
            np.random.shuffle(keys)
            shuffled_data_dict = dict()
            for key in keys:
                shuffled_data_dict.update({key: data[key]})
            # pdb.set_trace()
            data = shuffled_data_dict
            # -------------
            for key in data.keys():
                jpg_file = join(path, number, key.split(".")[0] + ".jpg")
                output, indices = data[key]
                if manipulation_function is not None:
                    transform = list(map(manipulation_function, output))
                    indices = np.logical_xor(transform, indices)

                if exists(jpg_file):
                    continue
                # Here the plotting happens
                figure(figsize=(7, 7), dpi=16)
                plt.subplot(111, aspect="equal")
                function(output, indices, **params)
                plt.xlim(-1, 1)
                plt.ylim(-1, 1)
                plt.axis("off")
                plt.subplots_adjust(
                    left=0, bottom=0, right=1, top=1, wspace=0, hspace=0
                )
                plt.savefig(jpg_file)
                plt.close()


def create_dots_img(output: np.ndarray, indices: np.ndarray, Plate_Dic: Dict) -> None:
    """This function takes a list of circles, their indicators, and a dictionary
    containing the necessary information for plotting. The function reduces each circle
    into a dot. Depending on the configurations, a number of (connected or
    disconnected) dots at the circumference of each circle can be plotted.
    """
    num_random_points_fg, color_fg, connected_fg = (
        Plate_Dic["num_random_points_fg"],
        Plate_Dic["color_fg"],
        Plate_Dic["connected_fg"],
    )
    num_random_points_bg, color_bg, connected_bg = (
        Plate_Dic["num_random_points_bg"],
        Plate_Dic["color_bg"],
        Plate_Dic["connected_bg"],
    )

    foreground, background = output[indices], output[np.logical_not(indices)]
    plotpoints(foreground, num_random_points_fg, color_fg, connected_fg)
    plotpoints(background, num_random_points_bg, color_bg, connected_bg)


def create_circles_img(
    output: np.ndarray, indices: np.ndarray, Plate_Dic: Dict
) -> None:
    """This function calls the ishiharaMC library for plotting the foreground and
    background circles."""
    color_fg, color_bg = Plate_Dic["color_fg"], Plate_Dic["color_bg"]

    foreground, background = output[indices], output[np.logical_not(indices)]
    ishiharaMC.plotIshi(foreground, color=color_fg)
    ishiharaMC.plotIshi(background, color=color_bg)


def plot_transform(
    output: np.ndarray,
    idx_final: np.ndarray,
    transform_function: Callable,
    plot_function: Callable,
    Plate_Dic: Dict,
) -> None:
    """This function calls one of the plate plotting functions after performing one of
    the plate manipulation functions."""
    transform = list(map(transform_function, output))
    new_index = np.logical_xor(transform, idx_final)
    plot_function(output, new_index, Plate_Dic)
