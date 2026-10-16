---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hello! I'm **Jun-Hsiang Yao (姚闰翔)**. I am currently a Ph.D. student in the School of Data Science at Fudan University, advised by Prof. [Siming Chen](http://simingchen.me/), and a member of the [FDU-VIS Lab](https://fduvis.net/). I received my master's degree in Applied Statistics from Fudan University.

My research interests lie at the intersection of **Augmented and Virtual Reality (AR/VR), Human-Computer Interaction (HCI), and Data Visualization (VIS)**. My research explores how AR/VR and AI can enable situated and context-aware interactions that augment human capabilities, with particular interests in supporting information perception and understanding, learning, communication, and collaboration across physical, virtual, and hybrid environments.

Welcome to my personal website. Feel free to look around!


<!-- # 🔥 News
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. -->

# 📝 Publications

<p class="jun-equal-note">* denotes equal contribution.</p>


<style>
/* Scoped styles: will only affect the Publications section. */
.jun-publications { margin-top: 0.8rem; }
.jun-publications .jun-pub-item {
  display: flex;
  flex-wrap: nowrap;
  align-items: flex-start;
  gap: 18px;
  padding: 22px 0;
  border-bottom: 1px solid #e5e7eb;
}
.jun-publications .jun-pub-image {
  flex: 0 0 235px;
  max-width: 29%;
  display: block;
}
.jun-publications .jun-pub-image img {
  display: block;
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: contain;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  box-shadow: none;
}
.jun-publications .jun-pub-text {
  flex: 1 1 0%;
  min-width: 0;
}
.jun-publications .jun-pub-title {
  margin: 0 0 5px;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.35;
}
.jun-publications .jun-pub-title a { color: inherit; text-decoration: none; }
.jun-publications .jun-pub-title a:hover { color: #287bb5; }
.jun-publications .jun-pub-authors {
  margin: 0 0 5px;
  line-height: 1.5;
}
.jun-publications .jun-pub-authors u {
  text-decoration: underline !important;
  text-underline-offset: 2px;
  border: 0;
}
.jun-publications .jun-pub-venue {
  margin: 0 0 9px;
  color: #59616e;
  line-height: 1.5;
}
.jun-publications .jun-pub-tag {
  display: inline-block;
  margin-right: 7px;
  padding: 0px 7px;
  border: 1px solid #e775a1;
  border-radius: 5px;
  color: #b5316b;
  font-weight: 600;
  font-size: 0.87em;
  background: #fff7fa;
}
.jun-publications .jun-pub-links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 2px;
}

.jun-publications .jun-pub-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 11px;
  border: 1px solid #d9dee5;
  border-radius: 999px;
  color: #4b5563;
  background: #f8fafc;
  text-decoration: none !important;
  font-size: 0.86em;
  font-weight: 600;
  line-height: 1.2;
  transition: all 0.18s ease;
}

.jun-publications .jun-pub-link i {
  font-size: 0.92em;
}

.jun-publications .jun-pub-link:hover {
  transform: translateY(-1px);
}

/* Paper */
.jun-publications .jun-pub-link--paper:hover {
  color: #256da8;
  border-color: #9fc5e3;
  background: #f3f9fd;
}

/* Demo */
.jun-publications .jun-pub-link--demo:hover {
  color: #b44747;
  border-color: #e2b0b0;
  background: #fff7f7;
}

/* Slides */
.jun-publications .jun-pub-link--slides:hover {
  color: #70529a;
  border-color: #c6b4dd;
  background: #faf7fd;
}
@media (max-width: 680px) {
  .jun-publications .jun-pub-item { flex-direction: column; gap: 12px; }
  .jun-publications .jun-pub-image { flex: none; max-width: 100%; width: 100%; }
  .jun-publications .jun-pub-image img { max-width: 440px; }
}

.jun-equal-note {
  margin: 0.1rem 0 1rem 0;
  font-size: 0.5rem;
  line-height: 1;
  color: #7a8088;
}
</style>

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition]\([https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf))

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[\*\*Project\*\*]\([https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC](https://scholar.google.com/citations?view_op=view_citation\&hl=zh-CN\&user=DhtAFkwAAAAJ\&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC)) \<strong>\<span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'>\</span>\</strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div> -->


<div class="jun-publications">

  <article class="jun-pub-item">
    <a class="jun-pub-image" href="https://doi.org/10.1109/TVCG.2026.3730177" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/papers/genlyph.PNG' | relative_url }}" alt="Gen-lyph: A Human–AI Collaboration System for Creating Figurative Glyph-Based Visualizations" loading="lazy">
    </a>
    <div class="jun-pub-text">
      <h3 class="jun-pub-title"><a href="https://doi.org/10.1109/TVCG.2026.3730177" target="_blank" rel="noopener noreferrer">Gen-lyph: A Human–AI Collaboration System for Creating Figurative Glyph-Based Visualizations</a></h3>
      <p class="jun-pub-authors">Jielin Feng, Xuan Chen, Xinwu Ye, <strong><u>Jun-Hsiang Yao</u></strong>, Zhuoheng Li, Laura Koesten, Xingyu Lan, Torsten Möller, Siming Chen</p>
      <p class="jun-pub-venue"><span class="jun-pub-tag">TVCG</span>IEEE Transactions on Visualization and Computer Graphics, 2026</p>
      <div class="jun-pub-links">
        <a class="jun-pub-link jun-pub-link--paper"
          href="https://doi.org/10.1109/TVCG.2026.3730177"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-file-alt" aria-hidden="true"></i>
          Paper
        </a>
      </div>
    </div>
  </article>

  <article class="jun-pub-item">
    <a class="jun-pub-image" href="https://doi.org/10.1145/3772318.3791844" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/papers/infoalign.PNG' | relative_url }}" alt="InfoAlign: A Human–AI Co-Creation System for Storytelling with Infographics" loading="lazy">
    </a>
    <div class="jun-pub-text">
      <h3 class="jun-pub-title"><a href="https://doi.org/10.1145/3772318.3791844" target="_blank" rel="noopener noreferrer">InfoAlign: A Human–AI Co-Creation System for Storytelling with Infographics</a></h3>
      <p class="jun-pub-authors">Jielin Feng, Xinwu Ye, Qianhui Li, Verena Prantl, <strong><u>Jun-Hsiang Yao</u></strong>, Yuheng Zhao, Yun Wang, Siming Chen</p>
      <p class="jun-pub-venue"><span class="jun-pub-tag">CHI</span>Proceedings of the CHI Conference on Human Factors in Computing Systems, 2026</p>
      <div class="jun-pub-links">
        <a class="jun-pub-link jun-pub-link--paper"
          href="https://doi.org/10.1145/3772318.3791844"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-file-alt" aria-hidden="true"></i>
          Paper
        </a>
      </div>
    </div>
  </article>

  <article class="jun-pub-item">
    <a class="jun-pub-image" href="https://doi.org/10.1016/j.visinf.2025.100301" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/papers/spatial.PNG' | relative_url }}" alt="Enhancing spatial learning under visual cues: A comparative study of virtual environments and perspectives" loading="lazy">
    </a>
    <div class="jun-pub-text">
      <h3 class="jun-pub-title"><a href="https://doi.org/10.1016/j.visinf.2025.100301" target="_blank" rel="noopener noreferrer">Enhancing spatial learning under visual cues: A comparative study of virtual environments and perspectives</a></h3>
      <p class="jun-pub-authors">Yifei Zhang, Lizhe Chen, <strong><u>Jun-Hsiang Yao</u></strong>, Zhan Wang, Siming Chen</p>
      <p class="jun-pub-venue"><span class="jun-pub-tag">VI</span>Visual Informatics, 2026</p>
      <div class="jun-pub-links">
        <a class="jun-pub-link jun-pub-link--paper"
          href="https://doi.org/10.1016/j.visinf.2025.100301"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-file-alt" aria-hidden="true"></i>
          Paper
        </a>
      </div>
    </div>
  </article>

  <article class="jun-pub-item">
    <a class="jun-pub-image" href="https://openreview.net/forum?id=BE7K2Id7yh" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/papers/motionmimic.PNG' | relative_url }}" alt="VidAnimator: User-Guided Stylized 3D Character Animation from Human Videos" loading="lazy">
    </a>
    <div class="jun-pub-text">
      <h3 class="jun-pub-title"><a href="https://openreview.net/forum?id=BE7K2Id7yh" target="_blank" rel="noopener noreferrer">VidAnimator: User-Guided Stylized 3D Character Animation from Human Videos</a></h3>
      <p class="jun-pub-authors">Xinwu Ye<sup>*</sup>, <strong><u>Jun-Hsiang Yao</u></strong><sup>*</sup>, Jielin Feng, Shuhong Mei, Xingyu Lan, Siming Chen</p>
      <p class="jun-pub-venue"><span class="jun-pub-tag">ICML Workshop</span>GlobalSouthML Workshop at ICML 2026</p>
      <div class="jun-pub-links">
        <a class="jun-pub-link jun-pub-link--paper"
          href="https://arxiv.org/pdf/2508.01878"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-file-alt" aria-hidden="true"></i>
          Paper
        </a>

        <a class="jun-pub-link jun-pub-link--demo"
          href="https://www.youtube.com/watch?v=8NR426QsNCc"
          target="_blank" rel="noopener noreferrer">
          <i class="fab fa-youtube" aria-hidden="true"></i>
          Demo
        </a>
      </div>
    </div>
  </article>

  <article class="jun-pub-item">
    <a class="jun-pub-image" href="https://doi.org/10.1109/TVCG.2025.3634638" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/papers/tennisvr.PNG' | relative_url }}" alt="Beyond the Broadcast: Enhancing VR Tennis Broadcasting through Embedded Visualizations and Camera Techniques" loading="lazy">
    </a>
    <div class="jun-pub-text">
      <h3 class="jun-pub-title"><a href="https://doi.org/10.1109/TVCG.2025.3634638" target="_blank" rel="noopener noreferrer">Beyond the Broadcast: Enhancing VR Tennis Broadcasting through Embedded Visualizations and Camera Techniques</a></h3>
      <p class="jun-pub-authors"><strong><u>Jun-Hsiang Yao</u></strong>, Jielin Feng, Xinfang Tian, Kai Xu, Gulshat Amirkhanova, Siming Chen</p>
      <p class="jun-pub-venue"><span class="jun-pub-tag">TVCG</span>IEEE Transactions on Visualization and Computer Graphics, 2026</p>
      <div class="jun-pub-links">
        <a class="jun-pub-link jun-pub-link--paper"
          href="https://doi.org/10.1109/TVCG.2025.3634638"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-file-alt" aria-hidden="true"></i>
          Paper
        </a>

        <a class="jun-pub-link jun-pub-link--demo"
          href="https://www.youtube.com/watch?v=qaT6_T7XxJ0"
          target="_blank" rel="noopener noreferrer">
          <i class="fab fa-youtube" aria-hidden="true"></i>
          Demo
        </a>

        <a class="jun-pub-link jun-pub-link--slides"
          href="{{ '/images/slides/TVCG-BeyondBroadcast-Slides.pdf' | relative_url }}"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-images" aria-hidden="true"></i>
          Slides
        </a>
      </div>
    </div>
  </article>

  <article class="jun-pub-item">
    <a class="jun-pub-image" href="https://doi.org/10.1109/TVCG.2025.3567135" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/papers/dtbia.PNG' | relative_url }}" alt="DTBIA: An Immersive Visual Analytics System for Brain-Inspired Research" loading="lazy">
    </a>
    <div class="jun-pub-text">
      <h3 class="jun-pub-title"><a href="https://doi.org/10.1109/TVCG.2025.3567135" target="_blank" rel="noopener noreferrer">DTBIA: An Immersive Visual Analytics System for Brain-Inspired Research</a></h3>
      <p class="jun-pub-authors"><strong><u>Jun-Hsiang Yao</u></strong>, Mingzheng Li, Jiayi Liu, Yuxiao Li, Jielin Feng, Jun Han, Qibao Zheng, Jianfeng Feng, Siming Chen</p>
      <p class="jun-pub-venue"><span class="jun-pub-tag">TVCG</span>IEEE Transactions on Visualization and Computer Graphics, 2025</p>
      <div class="jun-pub-links">
        <a class="jun-pub-link jun-pub-link--paper"
          href="https://doi.org/10.1109/TVCG.2025.3567135"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-file-alt" aria-hidden="true"></i>
          Paper
        </a>

        <a class="jun-pub-link jun-pub-link--demo"
          href="https://www.youtube.com/watch?v=Tq6sS4bgtmk"
          target="_blank" rel="noopener noreferrer">
          <i class="fab fa-youtube" aria-hidden="true"></i>
          Demo
        </a>

        <a class="jun-pub-link jun-pub-link--slides"
          href="{{ '/images/slides/TVCG-DTBIA-Slides.pdf' | relative_url }}"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-images" aria-hidden="true"></i>
          Slides
        </a>
      </div>
    </div>
  </article>

  <article class="jun-pub-item">
    <a class="jun-pub-image" href="https://doi.org/10.1109/PacificVis64226.2025.00026" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/images/papers/socialisland.PNG' | relative_url }}" alt="Social Media Island: Interactive User Profiling and Information Diffusion Exploration with 3D Visual Metaphors" loading="lazy">
    </a>
    <div class="jun-pub-text">
      <h3 class="jun-pub-title"><a href="https://doi.org/10.1109/PacificVis64226.2025.00026" target="_blank" rel="noopener noreferrer">Social Media Island: Interactive User Profiling and Information Diffusion Exploration with 3D Visual Metaphors</a></h3>
      <p class="jun-pub-authors">Jinjing Jiang<sup>*</sup>, Yuheng Zhao<sup>*</sup>, <strong><u>Jun-Hsiang Yao</u></strong>, Huiting Wang, Xuexi Wang, Lana Blue, Chen Guo, Xudong Li, Siming Chen</p>
      <p class="jun-pub-venue"><span class="jun-pub-tag">PacificVis</span>IEEE Pacific Visualization Conference (PacificVis), 2025</p>
      <div class="jun-pub-links">
        <a class="jun-pub-link jun-pub-link--paper"
          href="https://doi.org/10.1109/PacificVis64226.2025.00026"
          target="_blank" rel="noopener noreferrer">
          <i class="fas fa-file-alt" aria-hidden="true"></i>
          Paper
        </a>
      </div>
    </div>
  </article>

</div>


<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. -->

<!-- # 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->
