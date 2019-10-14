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

cnt = 0
for pre_data_line in pre_data_lines:
 pre_key = ' '.join(pre_data_line.split(' ')[0:2])
 for post_data_line in post_data_lines[cnt:]:
  post_key = ' '.join(post_data_line.split(' ')[0:2])
  if pre_key == post_key:
   cnt += 1
   pre_data_line = pre_data_line.replace('\n', '')
   post_data_line = post_data_line.replace('\n', '')
   pre_sent = ' '.join(pre_data_line.split(' ')[2:])
   post_sent = ' '.join(post_data_line.split(' ')[2:])
   maches = re.findall(p, pre_sent)
   for mach in maches:
    pre_sent = pre_sent.replace(mach, '')
   maches = re.findall(p2, pre_sent)
   for mach in maches:
    pre_sent = pre_sent.replace(mach, '')
   maches = re.findall(p, post_sent)
   for mach in maches:
    post_sent = post_sent.replace(mach, '')
   maches = re.findall(p2, post_sent)
   for mach in maches:
    post_sent = post_sent.replace(mach, '')
   output_sent = ''
   pre_sent = pre_sent.strip()
   post_sent = post_sent.strip()
   if len(pre_sent) < 1 or len(post_sent) < 1:
    continue
   pre_words = api.analyze(pre_sent)
   post_words = api.analyze(post_sent)
   pre_sent = ''
   for word in pre_words:
    for morph in word.morphs:
     if morph.tag == 'SL':
      continue
     text = morph.lex
     pre_sent += text
     pre_sent += ' '
   pre_sent = pre_sent.strip()
   if len(pre_sent) < 1:
    continue
   post_sent = ''
   for word in post_words:
    for morph in word.morphs:
     if morph.tag == 'SL':
      continue
     text = morph.lex
     post_sent += text
     post_sent += ' '
   post_sent = post_sent.strip()
   if len(post_sent) < 1:
    continue
   output_sent += pre_sent
   output_sent += '\t'
   output_sent += post_sent
   output_data.write(output_sent.strip() + '\n')
   break

output_data.close()
