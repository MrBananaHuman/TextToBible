from khaiii import KhaiiiApi
import re

p = re.compile('\(.+\)')
p2 = re.compile('\[.+\]')

api = KhaiiiApi()

pre_data = open('pre.txt', 'r', encoding='utf-8')
post_data = open('post.txt', 'r', encoding='utf-8')
output_data = open('preprocessed_data.txt', 'w', encoding='utf-8')

pre_data_lines = pre_data.readlines()
post_data_lines = post_data.readlines()

for i in range(0, len(pre_data_lines)):
 pre_data_line = pre_data_lines[i].replace('\n', '')
 pre_sent = ' '.join(pre_data_line.split(' ')[2:])
 maches = re.findall(p, pre_sent)
 for mach in maches:
  pre_sent = pre_sent.replace(mach, '')
 maches = re.findall(p2, pre_sent)
 for mach in maches:
  pre_sent = pre_sent.replace(mach, '')  
 pre_key = ' '.join(pre_data_line.split(' ')[0:1])
 post_data_line = post_data_lines[i].replace('\n', '')
 post_sent = ' '.join(post_data_line.split(' ')[2:])
 maches = re.findall(p, post_sent)
 for mach in maches:
  post_sent = post_sent.replace(mach, '')
 maches = re.findall(p2, post_sent)
 for mach in maches:
  post_sent = post_sent.replace(mach, '')
 post_key = ' '.join(post_data_line.split(' ')[0:1])
 if pre_key != post_key:
  continue
 else:
  output_sent = ''
  pre_sent = pre_sent.strip()
  post_sent = post_sent.strip()
  if len(pre_sent) < 1 or len(post_sent) < 1:
   continue
  pre_words = api.analyze(pre_sent)
  post_words = api.analyze(post_sent)
  for word in pre_words:
   for morph in word.morphs:
    if morph.tag == 'SL':
     continue
    text = morph.lex
    output_sent += text
    output_sent += ' '
  output_sent += '\t'
  for word in post_words:
   for morph in word.morphs:
    if morph.tag == 'SL':
     continue
    text = morph.lex
    output_sent += text
    output_sent += ' '
  output_data.write(output_sent.strip() + '\n')

output_data.close()
