#  Python package `ishihara-like-mnist`
#
#  file: export_import_images.py
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
   This Script can be used to transform images into tensors and vice versa.
   Examples:
        Export images to pickle files (only 10 images from each folder):
        ```
            python IshiharaImagesExportImport.py --Plate_path Output\\Only_Circles \
            --output_path Output --out_folder_name Only_Circles_pickle --mode 0 \
            --MaxImages 5
        ```
        Export tensors in pickle files into images (only 10 images from each folder):
        ```
            python IshiharaImagesExportImport.py --Plate_path \
            Output\\Only_Circles_pickle --output_path Output --out_folder_name \
            Only_Circles_new --mode 1 --MaxImages 10
        ```
"""

import argparse
import errno
import os
import pickle
from os import listdir
from os.path import exists, isdir, isfile, join
from typing import Any, Dict

import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from matplotlib.pyplot import figure
from PIL import Image

import IshiharaSimulate.plates as plates


def files_to_tensort(files: Dict, path: str) -> Dict:
    """This function reads image files and transforms them into tensors."""
    transform = transforms.Compose([transforms.PILToTensor()])
    files_dic: Any = {k: dict() for k in files.keys()}
    ids = 0
    for k in files.keys():
        for i, f in enumerate(files[k]):
            if i > args.MaxImages and args.MaxImages != -1:
                break

            ids += 1
            if ids % 1000 == 0:
                print(ids, path, k, f)
            file = join(path, k, f)
            image = Image.open(file)
            img_tensor = transform(image)
            files_dic[k][f] = img_tensor / 255
    return files_dic


def export_Images_from_Pickle(args: argparse.Namespace) -> None:
    """This function reads tensors from pickle files and exports them into images."""
    plates.create_folder_tree(args.output_path, args.out_folder_name)

    for t in ["Test_images", "Train_images"]:
        plate_path = join(args.Plate_path, t)
        pickle_file = join(plate_path, t + ".pickle")

        files_dic = load_pickle(pickle_file)
        for nr in files_dic:
            print(nr)
            for i, f in enumerate(files_dic[nr].keys()):
                if i > args.MaxImages and args.MaxImages != -1:
                    break
                print(f)
                image = transforms.ToPILImage()(files_dic[nr][f])
                jpg_file = join(args.output_path, args.out_folder_name, t, nr, f)

                figure(figsize=(7, 7), dpi=16)
                ax = plt.subplot(111, aspect="equal")
                ax.imshow(image)
                plt.axis("off")
                plt.subplots_adjust(
                    left=0, bottom=0, right=1, top=1, wspace=0, hspace=0
                )
                plt.savefig(jpg_file)
                plt.close()


def load_pickle(pickle_file: str) -> Dict:
    """This function reads a pickle file and returns a dictionary of tensors."""
    if exists(pickle_file):
        print("loading", pickle_file)
        with open(pickle_file, "rb") as file:
            data = pickle.load(file)
            files_dic = data["files_dic"]
        print("loaded", pickle_file)
        return files_dic
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pickle_file)


def export_Images_to_Pickle(args: argparse.Namespace) -> None:
    """This function reads images and exports them as pickle files of tensors."""
    plates.create_folder_tree(args.output_path, args.out_folder_name, True)

    for t in ["Test_images", "Train_images"]:
        task_path = join(args.Plate_path, t)
        onlyfolders = [f for f in listdir(task_path) if isdir(join(task_path, f))]
        files = {
            F1: [
                f
                for f in listdir(join(task_path, F1))
                if isfile(join(task_path, F1, f)) and ".jpg" in f
            ]
            for F1 in onlyfolders
        }

        files_dic = files_to_tensort(files, task_path)

        pickle_file = join(args.output_path, args.out_folder_name, t, t + ".pickle")
        result_dic = {"files_dic": files_dic}
        with open(pickle_file, "wb") as file:
            pickle.dump(result_dic, file)

    return


if __name__ == "__main__":

    # pdb.set_trace()
    # data parameters
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--Plate_path", default="data/", help="path where data is located"
    )
    parser.add_argument(
        "--output_path", help="Where to save the data.", type=str, default="."
    )
    parser.add_argument(
        "--out_folder_name",
        help="What is the name of the output folder",
        type=str,
        default="OutputPlate",
    )
    parser.add_argument(
        "--MaxImages",
        help="Maximum number of images to be imported or exported per class. "
        "Ignored when -1",
        type=int,
        default=-1,
    )

    parser.add_argument(
        "--mode",
        help="0:(Default )Export images to pickle, 1:Export images from pickle",
        type=int,
        default=0,
    )

    args = parser.parse_args()
    if args.mode == 0:
        export_Images_to_Pickle(args)
    elif args.mode == 1:
        export_Images_from_Pickle(args)
