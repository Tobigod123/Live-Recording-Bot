o
    �!'c O  �                   @   sH  d dl mZmZmZmZ d dlZd dlmZmZm	Z	 d dl
Z
d dlZd dlZd dlmZ d dlZd dlmZmZ d dlmZ d dlmZ d dlZd dlZd dlZd dlmZ d dlZd dlZd d	lT d dlZe
j d
e
�!d�e
�"� ge
j#d� e
�$e%�Z&e'�(d� e)e'7 Z)i Z*dZ+edej,�-d�e.ej,�-d��ej,�-d�d�Z/ddddddd�Z0dddddd d�Z1d!d"d#d$d%d&d�Z2ej,�-d'd(�Z3d)d*� Z4d+d,� Z5d-d.� Z6e/�7e�8d/d0g�e�9e'�@ �d_d2d3��Z:e/�7ej;e�8d4g�@ �d_d5d6��Z<e/�7ej;ej=d7d8�@ �d9ed:ed1dfd;d<��Z>e/�7ej;e�8d=�@ �d9ed:ed1dfd>d<��Z>e/�?e�=d?��d9ed@efdAdB��Z@e/�?e�=dC��d9edDefdEdB��Z@d1eAfdFdG�ZBdHdI� ZCdJeAdKedLeAfdMdN�ZDdOdP� ZEdQdR� ZFdSeAd1eeAeAe.e.f fdTdU�ZGdVdW� ZHdXdY� ZIdZe.d1eAfd[d\�ZJejK�Le3��s�e�Me3� e4�  e/�N�  e&�Od]� e	�  e&�Od^� e/�P�  dS )`�    )�Message�CallbackQuery�InlineKeyboardMarkup�InlineKeyboardButtonN)�Client�filters�idle)�Tuple)�join�exists)�extractMetadata)�createParser)�UserNotParticipant)�*z4%(asctime)s - %(name)s - %(levelname)s - %(message)s�log.txt)�format�handlers�leveli���Gzy^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$ZpaidbotZ	BOT_TOKENZAPI_IDZAPI_HASH)Z	bot_tokenZapi_idZapi_hashZ420Z3600Z5400Z7200Z9000Z10800)z0:30z1:00z1:30z2:00z2:30z3:00z00:7:00z01:00;00z01:30:00z02:00:00z02:30:00z03:00:00Z30Min�1Hourz	1hr 30min�2Hourz	2hr 30minZ3Hour�DOWNLOAD_DIRECTORYz./downloadsc                  C   s�   d} d}t �d| � d|� d��}|jdkr;t�|j�}|�dd�dkr8t�|�d	d
�� t�d� t	�
d� d S 	 d S t�d
� t�d� t	�
d� d S )NZ e36aa74fd74e71e1a03fd513742de242Zliverecz2https://gist.githubusercontent.com/Jigarvarma2005/z/raw/z.txt��   �status�0�msgzThis code has been expiredzExiting now!�   )�requests�getZstatus_code�json�loadsZcontent�_LOG�error�info�sys�exit)Zmy_idZmyyy_jddtegZreq_Zjsn� r%   �main.py�	check_botJ   s   



r'   c                 �   s�   �t ro| �tt ��I d H }z%| �tt �|jj�I d H }|jdkr0| j|jjddd�I d H  W dS W d S  tyX   | j|jjdt	t
d|jd�gt
d	d
d�gg�d�I d H  Y dS  tyn   | j|jjddd�I d H  Y dS w d S )N�kicked�[Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/JV_Community).T)�chat_id�text�disable_web_page_preview�  zo**Please Join My Updates Channel to use this Bot!**

Due to Overload, Only Channel Subscribers can use the Bot!�   🤖 Join Updates Channel��url�   🔄 Refresh 🔄�
refreshmeh�Zcallback_data)r*   r+   �reply_markup�LSomething went Wrong. Contact my [Support Group](https://t.me/JV_Community).)�UPDATES_CHANNEL�create_chat_invite_link�int�get_chat_member�	from_user�idr   Zsend_messager   r   r   �invite_link�	Exception)�bot�cmdr<   �userr%   r%   r&   �handle_force_sub[   sF   �
���
�������rA   c              
   �   s�   �zXt | jj�tv rKtt | jj� }tt�� | �tk rCdtttt | jj� �t tt�� � d �� d�}| j|dd�I dH  W dS t| jj= W dS tt�� �tt | jj�< W dS  t	yq } zt
�|� W Y d}~dS d}~ww )zPChecking the time gap is completed or not 
    and checking the parallel processzPlease wait ��  z before sending new request.T)r+   �quoteNF)�strr:   r;   �TIME_GAP_STOREr8   �timeZTIME_GAP�TimeFormatter�
reply_textr=   r    �	exception)�mZpr_timer+   �er%   r%   r&   �timegap_check�   s(   �4�

��rL   �logZlogs�returnc              
   �   sJ   �z|� d�I d H  W d S  ty$ } zt�|� W Y d }~d S d }~ww )Nr   )Zreply_documentr=   r    rI   )r>   �messagerK   r%   r%   r&   �
get_log_wm�   s   ���rP   �startc                 �   �^   �t | |�I d H }|dkrd S 	 |jdttddd�tddd�gtdd	d�gg�d
�I d H  d S )Nr-   z�hey there, i am live video recorder bot, i can record live video using its url

**note: Don't report to Devloper if video duration time wrong**

by @Universal_Projects�   🚨Updates Channel🚨�https://t.me/Universal_Projectsr/   �   👷Support Group👷�https://t.me/JV_Community�   🧑‍💻Devloper🧑‍💻�"https://github.com/Jigarvarma2005/�r+   r4   �rA   rH   r   r   �r>   rO   �backr%   r%   r&   �get_help�   �   �

�
����r]   z.*http.*)�patternr>   rO   c           
      �   s`  �t | |�I d H }|dkrd S 	 |j�d�}t|�dkr%|jdd�I d H S |�d�I d H }|d }t|�\}}|sA|�|�I d H S t|d �}t|�d	��d
krY|jdd�I d H S t|�	d	d��}t|�
d	d�d �	d	d��dkr�|jjtvr�|jdttddd�tddd�gtddd�gg�d�I d H S |jjtvr�t|�I d H }	|	r�d S t|||�I d H  d S )Nr-   � �   zVPlease send link in below format, check /help to know more

`link timestamp(hh:mm:ss)`�r+   zPlease wait ....r   r   �:�   � �2   zwMaximum time limit is 50minutes.
ask in support group to get personal bot without any limit

**Warn:- Nothing is free**rS   rT   r/   rU   rV   rW   rX   rY   )rA   r+   �split�lenrH   �
directLink�editrD   r8   �replace�rsplitr:   r;   �
AUTH_USERSr   r   rL   �uploader_main)
r>   rO   r\   Zurl_msgZmsg_r0   Zis_okZtimessZ	timelimitZtime_gapr%   r%   r&   �	main_func�   sB   �,

�
����ro   �helpc                 �   rR   )Nr-   z�To record a live link send your link in below format, 

 `link timestamp`

**Example:**
https://example.com/live-link.m3u8 00:05:00

timestamp==hh:mm:ss

**note: Don't report to Devloper if video duration time wrong**

by @Universal_ProjectsrS   rT   r/   rU   rV   rW   rX   rY   rZ   r[   r%   r%   r&   ro   �   r^   ztime.*?�cbc                 �   sB   �|j �dd�d }|j}|jj�d�d }t|||�I d H  d S )N�_r   r`   r   )�datarg   rO   Zreply_to_messager+   rn   )r>   rq   �cb_datar   Z	user_linkr%   r%   r&   �cb_handler_main�   s
   �ru   zrefreshmeh.*?�queryc                 �   s�   �|j dkrytrn| �tt��I d H }z#| �tt�|jjj�I d H }|jdkr4|jj	ddd�I d H  W d S W n8 t
yY   |jj	dttd|jd�gtd	dd
�gg�d�I d H  Y d S  tym   |jj	ddd�I d H  Y d S w |j�	d�I d H  d S d S )Nr2   r(   r)   T)r+   r,   u�   **You Still Didn't Join ☹️, Please Join My Updates Channel to use this Bot!**

Due to Overload, Only Channel Subscribers can use the Bot!r.   r/   r1   r3   rY   r5   z Now you can use me, check /start)rs   r6   r7   r8   r9   rO   Zchatr;   r   rj   r   r   r   r<   r=   )r>   rv   r<   r@   r%   r%   r&   ru   �   sD   �

���
�������c                 C   sV   t �t| �}|r'tjd| � �dtjd�}t|j�� �	d��}t
�|� d|fS d| fS )Nz
yt-dlp -g T)�shell�stdout�utf-8)�re�match�yt_regex�
subprocess�Popen�PIPErD   rx   �read�decoder    r"   )�linkZytlinkZsubcallZlinkchekr%   r%   r&   ri   "  s   
ri   c                 C   sP   t �| �}t� }|D ]}t j�| |�}t j�|�r |t|� }q
|�|� q
|S )N)�os�listdir�list�pathr
   �isdir�getListOfFiles�append)ZdirNameZ
listOfFileZallFiles�entryZfullPathr%   r%   r&   r�   +  s   
r�   �usr_linkr   rt   c                 �   s�  �t �  |j|� d�d d�I d H  tttt�� ��}tj�|�s%t�	|� t|tt�� �d �}t
�d|� d| � �� d}d}d}d	}t|� d
|� d
|� d| � d|� d
|� d
|� ��I d H d }	|	rgt
�|	� 	 t|�r�z%t|�I d H }
|j||
d| � dt|
d �� d�t|t�� fd�I d H  W n; ty� } zt
�|� |�|�I d H  W Y d }~n!d }~ww d|	v r�|jd| � �dd�I d H  n
|jddd�I d H  zzt�|� W n   Y |�� I d H  W d S  ty� } zt
�|� W Y d }~d S d }~ww )Nz+ Recording started,
this will take time ...rY   z.mkvz
Recording z from Zffmpegz-probesize 10000000z*-analyzeduration 15000000 -timeout 9000000z--codec copy -map 0:v -map 0:a -ignore_unknownr`   z -i z -t r   zRecording done of z

Duration: rB   z

By @Universal_Projects)Zvideo�durationZcaption�progressZprogress_argszConnection timed outzConnection timed out with T)rC   z)Recording failed, probably link error ...)r'   rj   r
   r   rD   rF   r�   r�   r�   �makedirsr    r"   �runcmdr   �get_video_durationZreply_videorG   �progress_for_pyrogramr=   rI   rH   �shutil�rmtree�delete)r�   r   rt   Zvideo_dir_pathZvideo_file_pathZexe_nameZprobeZanylz�codecZerror_recording_videoZ
v_durationrK   r%   r%   r&   rn   <  s\   ��
:

�
��
��rn   c                 �   s,   �t t| ��}d}|�d�r|�d�j}|S )Nr   r�   )r   r   Zhasr   �seconds)Z
input_fileZmetadataZtotal_durationr%   r%   r&   r�   �  s   �
r�   c                   C   sJ   t tddd�tddd�gtddd�tdd	d�gtd
dd�tddd�gg�S )NZ30minz	time_0:30r3   r   z	time_1:00z	1Hr 30minz	time_1:30r   z	time_2:00z	2Hr 30minz	time_2:30Z3Hrz	time_3:00)r   r   r%   r%   r%   r&   �create_time_buttons�  s   

�

�

���r�   r?   c                 �   sn   �t �| �}tj|tjjtjjd��I dH }|�� I dH \}}|�dd��� }|�dd��� }|||j	|j
fS )z run command in terminal )rx   �stderrNry   rk   )�shlexrg   �asyncioZcreate_subprocess_execr}   r   Zcommunicater�   �strip�
returncodeZpid)r?   �argsZprocessrx   r�   r%   r%   r&   r�   �  s   �
��r�   c                 �   s@  �t � � }|| }t|d �dks| |kr�| d | }| | }t|�d }t||  | �d }	||	 }
d}d}t|d�}t|
d�}
d}zt|�}W n   d}Y td	d
�D ]}|t|d �krd||7 }qU||7 }qUd�t|d�|�}|d�t| �t|�t|�|
dkr�|
nd� }z|jd�|�d�I d H  W d S    Y d S d S )Ng      $@r   �d   rB   u   ▪️u   ▫️)�millisecondsre   r   �   �
   zUploading: {}%
[{}]
ra   z"{0} of {1}
Speed: {2}/sec
ETA: {3}z0 sz{}
 {}rb   )rF   �roundrG   r8   �ranger   �
humanbytesrj   )Zcurrent�totalrO   rQ   ZnowZdiffZ
percentageZspeedZelapsed_timeZtime_to_completionZestimated_total_time�compZncompZpr�ir�   �tmpr%   r%   r&   r�   �  sR   �



�����r�   c              
   C   sf   | sdS d}d}dddddd	d
ddd�	}| |kr$| | } |d7 }| |kst t| d��d ||  d S )Nre   i   r   r`   �K�M�G�T�P�E�Z�Y)	r   r   ra   �   rd   �   �   �   �   r   ra   �B)rD   r�   )�sizeZpower�nZ
Dic_powerNr%   r%   r&   r�   �  s   �r�   r�   c                 C   s�   t t| �d�\}} t |d�\}}t |d�\}}t |d�\}}|r&t|�d nd|r/t|�d nd |r9t|�d nd |rCt|�d nd | rMt| �d	 nd }|d d
� S )NrB   �<   �   zd, re   zh, zm, zs, zms, �����)�divmodr8   rD   )r�   r�   ZminutesZhoursZdaysr�   r%   r%   r&   rG   �  s   ����rG   zBot Started!zBot Stopped!)rN   N)QZpyrogram.typesr   r   r   r   r�   Zpyrogramr   r   r   �loggingr�   rF   �typingr	   r�   �os.pathr
   r   Zhachoir.metadatar   Zhachoir.parserr   r�   r   r   Zpyrogram.errorsr   rz   r}   ZConfigr#   ZbasicConfigZFileHandlerZStreamHandler�INFOZ	getLogger�__name__r    ZOWNER_IDr�   rm   rE   r|   �environr   r8   ZjvbotZTIME_VALUES_SECZTIME_VALUESZTIME_VALUES_STRr   r'   rA   rL   Z
on_messageZcommandr@   rP   Zprivater]   Zregexro   Zon_callback_queryru   rD   ri   r�   rn   r�   r�   r�   r�   r�   rG   r�   r�   r�   rQ   r"   �stopr%   r%   r%   r&   �<module>   s�   ��



�
���(&'	G2


