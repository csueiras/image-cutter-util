'''
Cut Image Utility
    Copyright 2012 Christian A. Sueiras
        
    -Utility to slice an image into tiles

Depends on:
    -Python Image Library (PIL)
    
#######################################################################################
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
#######################################################################################
'''

import sys
from PIL import Image

def explain_usage():
    print 'cut_image.py spritesheet_image_filename output_dir cell_width cell_height start_column start_row end_column end_row'
    
def main(spritesheet, output_dir, cell_width, cell_height, start_col, start_row, end_col, end_row):
    img = Image.open(spritesheet)
    for row in range(start_row, end_row):    
        for col in range(start_col, end_col):
            left = col * cell_width
            top = row * cell_height
            crop_box = (left, top, left + cell_width, top + cell_height)
            sprite = img.crop(crop_box)
            output_filename = output_dir+'/%d_%d.png' % (row, col)
            sprite.save(output_filename)
if __name__ == '__main__':
    if len(sys.argv) < 9:
        print 'Wrong number of arguments'
        explain_usage()
    else:
        print sys.argv
        main(spritesheet = sys.argv[1], output_dir = sys.argv[2], cell_width = int(sys.argv[3]), cell_height = int(sys.argv[4]),
             start_col = int(sys.argv[5]), start_row = int(sys.argv[6]), end_col = int(sys.argv[7]), end_row = int(sys.argv[8]))
