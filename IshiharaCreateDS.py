#  Python package `ishihara-like-mnist`
#
#  file: IshiharaCreateDS.py
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
   This Script can be used to transform circled MNIST into one of the Ishihara plates.
   It also contains uncolored manipulation functions.
   Examples:
            Creating the plate "only circles":
            ```
            python IshiharaCreateDS.py --data_path Output\\PFiles --out_path Output \
            --plate 20 --manipulation 1
            ```
            Creating the plate 1:
            ```
            python IshiharaCreateDS.py --data_path Output\\PFiles --out_path Output \
            --plate 1 --manipulation 1
            ```
            Creating the plate 4 with above_line manipulation:
            ```
            python IshiharaCreateDS.py --data_path Output\\PFiles --out_path Output \
            --plate 4 --manipulation 4
            ```

"""

import argparse
from os import listdir
from pathlib import Path
from typing import Any, Callable, Dict

import numpy as np

import IshiharaSimulate.plates as plates

Manipulation_dic: Dict[int, Dict[str, Any]] = {
    1: {"Function": None, "Name": "No_Manipulation"},  # No_Manipulation
    2: {"Function": lambda x: x[1] > 0, "Name": "upper_half"},  # upper_half
    3: {"Function": lambda x: x[0] > 0, "Name": "right_half"},  # right_half
    4: {"Function": lambda x: x[0] - x[1] < 0, "Name": "above_line"},  # above_line
    5: {
        "Function": lambda x: np.random.random_sample() > 0.85,
        "Name": "random15",
    },  # random15
    6: {
        "Function": lambda x: (x[0] > 0) ^ (x[1] > 0),
        "Name": "chess_board",
    },  # chess_board
    7: {
        "Function": lambda x: (x[0] * 2 % 2 > 1) ^ (x[1] * 2 % 2 > 1),
        "Name": "chess2_board",
    },  # chess2_board
}

Plates: Dict[int, Dict[str, Any]] = {
    1: {
        "Function": plates.plot_plate_generic,
        "Name": "Plate_1",
        "Params": dict(Plate_Dic=plates.Plates_Dict[1]),
    },  # Plate_1
    2: {
        "Function": plates.plot_plate2,
        "Name": "Plate_2",
        "Params": dict(Plate_Dic=plates.Plates_Dict[2]),
    },  # Plate_2
    3: {
        "Function": plates.plot_plate3,
        "Name": "Plate_3",
        "Params": dict(Plate_Dic=plates.Plates_Dict[3]),
    },  # Plate_3
    4: {
        "Function": plates.plot_plate4,
        "Name": "Plate_4",
        "Params": dict(Plate_Dic=plates.Plates_Dict[4]),
    },  # Plate_4
    5: {
        "Function": plates.plot_plate5,
        "Name": "Plate_5",
        "Params": dict(Plate_Dic=plates.Plates_Dict[5]),
    },  # Plate_5
    6: {
        "Function": plates.plot_plate6,
        "Name": "Plate_6",
        "Params": dict(Plate_Dic=plates.Plates_Dict[6]),
    },  # Plate_6
    7: {
        "Function": plates.plot_plate7,
        "Name": "Plate_7",
        "Params": dict(Plate_Dic=plates.Plates_Dict[7]),
    },  # Plate_7
    8: {
        "Function": plates.plot_plate_generic,
        "Name": "Plate_8",
        "Params": dict(Plate_Dic=plates.Plates_Dict[8]),
    },  # Plate_8
    9: {
        "Function": plates.plot_plate_generic,
        "Name": "Plate_9",
        "Params": dict(Plate_Dic=plates.Plates_Dict[9]),
    },  # Plate_9
    10: {
        "Function": plates.plot_plate_generic,
        "Name": "Plate_10",
        "Params": dict(Plate_Dic=plates.Plates_Dict[10]),
    },  # Plate_10
    11: {
        "Function": plates.plot_plate_generic,
        "Name": "Plate_11",
        "Params": dict(Plate_Dic=plates.Plates_Dict[11]),
    },  # Plate_11
    12: {
        "Function": plates.plot_plate_generic,
        "Name": "Plate_12",
        "Params": dict(Plate_Dic=plates.Plates_Dict[12]),
    },  # Plate_12
    13: {
        "Function": plates.plot_plate_generic,
        "Name": "Plate_13",
        "Params": dict(Plate_Dic=plates.Plates_Dict[13]),
    },  # Plate_13
    16: {
        "Function": plates.plot_plate16_17,
        "Name": "Plate_16",
        "Params": dict(Plate_Dic=plates.Plates_Dict[16]),
    },  # Plate_16
    17: {
        "Function": plates.plot_plate16_17,
        "Name": "Plate_17",
        "Params": dict(Plate_Dic=plates.Plates_Dict[17]),
    },  # Plate_17
    20: {
        "Function": plates.create_circles_img,
        "Name": "Only_Circles",
        "Params": dict(Plate_Dic=dict(color_fg="k", color_bg="k")),
    },
    21: {
        "Function": plates.create_dots_img,
        "Name": "Only_Dots",
        "Params": dict(
            Plate_Dic=dict(
                color_fg="k",
                color_bg="k",
                num_random_points_fg=0,
                num_random_points_bg=0,
                connected_fg=False,
                connected_bg=False,
            )
        ),
    },
    22: {
        "Function": plates.create_dots_img,
        "Name": "Dots_10_disconnected",
        "Params": dict(
            Plate_Dic=dict(
                color_fg="k",
                color_bg="k",
                num_random_points_fg=10,
                num_random_points_bg=10,
                connected_fg=False,
                connected_bg=False,
            )
        ),
    },
    23: {
        "Function": plates.create_dots_img,
        "Name": "Dots_10_connected",
        "Params": dict(
            Plate_Dic=dict(
                color_fg="k",
                color_bg="k",
                num_random_points_fg=10,
                num_random_points_bg=10,
                connected_fg=True,
                connected_bg=True,
            )
        ),
    },
    30: {"Function": None, "Name": "Random_plates", "Params": None},
    31: {
        "Function": plates.plot_plate_random_color,
        "Name": "Random_colors",
        "Params": dict(Plate_Dic=dict(Plate_Dic=None)),
    },
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path", help="Where to find the data.", type=str, default="./datasets"
    )
    parser.add_argument(
        "--out_path", help="Where to save the data.", type=str, default="./datasets"
    )
    parser.add_argument(
        "--plate",
        help="Plates 1-13, 16, 17, Only_Circles = 20; Only_Dots = 21; "
        "Dots_10_disconnected = 22;Dots_10_connected = 23, Random_colors=31",
        type=int,
        default=1,
    )
    parser.add_argument(
        "--manipulation",
        help="1: No_Manipulation, 2: upper_half, 3: right_half, 4: above_line, 5: "
        "random15, 6: chess_board, 7: chess2_board",
        type=int,
        default=1,
    )

    args = parser.parse_args()

    mypath = args.data_path
    outpath = args.out_path
    plate = args.plate
    manipulation_method = args.manipulation

    # test_path = r"E:\Data\MNIST\result_test"
    test_path = str(Path(mypath) / "Test_images")
    test_files = [
        str(Path(test_path) / f) for f in listdir(test_path) if ".pickle" in f
    ]

    # train_path = r"E:\Data\MNIST\result_train"
    train_path = str(Path(mypath) / "Train_images")
    train_files = [
        str(Path(train_path) / f) for f in listdir(train_path) if ".pickle" in f
    ]

    # Running the creation
    F: Callable = Plates[plate]["Function"]
    params: Dict = Plates[plate]["Params"]

    manpF: Callable = Manipulation_dic[manipulation_method]["Function"]
    if manpF is not None:
        name = (
            str(Plates[plate]["Name"])
            + "_"
            + str(Manipulation_dic[manipulation_method]["Name"])
        )
    else:
        name = str(Plates[plate]["Name"])

    if plate == 30:
        plates.create_folder_tree(outpath, name)
        Ishi_Plates = [
            "Plate_1",
            "Plate_2",
            "Plate_3",
            "Plate_4",
            "Plate_5",
            "Plate_6",
            "Plate_7",
            "Plate_8",
            "Plate_9",
            "Plate_10",
            "Plate_11",
            "Plate_12",
            "Plate_13",
            "Plate_16",
            "Plate_17",
        ]
        plate.create_random_plates(
            test_files, outpath, name, "Test_images", Ishi_Plates
        )
        plate.create_random_plates(
            train_files, outpath, name, "Train_images", Ishi_Plates
        )
    else:
        # pdb.set_trace()
        plates.create_folder_tree(outpath, name)
        plates.process_files(
            test_files,
            F,
            manpF,
            str(Path(outpath) / name / "Test_images"),
            params,
        )
        plates.process_files(
            train_files,
            F,
            manpF,
            str(Path(outpath) / name / "Train_images"),
            params,
        )
