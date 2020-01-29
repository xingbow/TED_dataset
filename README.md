# VoiceCoach
This is the TED Talk dataset for VoiceCoach, CHI 2020, https://arxiv.org/abs/2001.07876.


# TED_dataset

The datasets contain meta information of 2623 TED Talks in official [TED.com](https://www.ted.com/) website until Jun 7th, 2019. 

The meta information includes fields: _'author', 'datefilmed', 'totalviews', 'comments', 'language', 'downloadlink', 'vidlen', 'aws-transcripts', 'datecrawled', 'datepublished', 'title', 'id', 'url', 'keywords', 'videoname', 'ratings'_, and complete information is stored in the field _'alldata_JSON'_.

## Fileds
- **url**: original video link
- **aws-transcripts**: Each video in the dataset is transcribed by AWS. It has two fileds, including:
  - *transcript*: all words in the video
  - *words*: an array containing detailed information about all words. e.g.,
    - "start_time": "12.94", 
    - "end_time": "13.25", 
    - "alternatives": [{"confidence": "0.9097", "content": "we"}], "type": "pronunciation"}]

(**updating**)

# Notice
If you use this dataset, please cite our paper

*VoiceCoach*: Interactive Evidence-based Training for Voice Modulation Skills in Public Speaking

Preprint: https://arxiv.org/abs/2001.07876

Authors: Xingbo Wang, Haipeng Zeng, Yong Wang, Aoyu Wu, Zhida Sun, Xiaojuan Ma, Huamin Qu


# Acknowledgements
The dataset is shared under the Creative Commons license.
