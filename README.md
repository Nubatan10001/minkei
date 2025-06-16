<p align="left"> 
  <img alt="Top Langs" height="150px" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Nubatan10001&layout=compact&count_private=true&show_icons=true&theme=onedark" />
  <img alt="github stats" height="150px" src="https://github-readme-stats.vercel.app/api?username=Nubatan10001&count_private=true&show_icons=true&show_icons=true&theme=onedark" />
</p>

[![trophy](https://github-profile-trophy.vercel.app/?username=Nubatan10001&theme=onedark&column=8
)](https://github.com/ryo-ma/github-profile-trophy)

## みんなの経済学！（みんけい！）とは？

大学で経済学を学んでいた頃、ひとつ悩みがありました。  
それは、「経済学を体系的に学べるプラットフォームが存在しない」ということです。

たとえば、大学数学や物理学なら  
[ヨビノリ](https://yobinori.jp/) や [KIT数学ナビケーション](https://w3e.kanazawa-it.ac.jp/math/video/henkan-tex.cgi?target=/math/video/index.html) のような  
誰でも気軽に学べる学習サイトやYouTubeチャンネルが充実しています。

一方、経済学は「入門編」「ゲーム理論」「計量経済学」など、テーマごとの情報はあるものの、  
**学部レベルの経済学全体をカバーするようなサイトはほとんど存在しません**でした。

そのため私は、大学の講義で詰まった際に必死についていくために難しい教科書を読み漁ったり、より簡単な教科書を買ったり、   
時には公務員試験用の参考書で問題演習をしたりしながら、学び続けていました。  
> ── 経済学にも、もっと「簡単に」かつ「気軽に」学べるような環境があればいいのに・・・。   

当時、私はそう感じていました。

そんな中、大学4年生にデータサイエンティストとして参加していた長期インターンにて、Python × Django を用いた分析プラットフォームの開発案件に関わる機会を得ました。  
このWebアプリ開発の経験を積む中で、ふと思ったのです。

> ── いまなら、自分で“経済学の学習サイト”を作れるかもしれない！

そうして生まれたのが、この Webサイト **『みんなの経済学！（みんけい！）』** です。  
主にDjangoを活用して、誰もが経済学を気軽に学べる環境を目指して開発を進めています。   

開発環境は、"minkei/minkei/requirements.txt" に記載してあります。

---

## ブランチ運用方針について（補足）

本プロジェクトでは、Djangoを用いた動的なコンテンツ管理（記事投稿・編集）機能を導入しており、**管理画面（admin）から直接データベースに情報を追加・修正**する形で運用しています。

通常のチーム開発においては以下のようなブランチ戦略が一般的だと認識しています。

- `main`：安定版のコードのみを置く
- `develop`：開発途中の機能を統合・テストする中間地点
- `feature/*`：各機能ごとに小さくブランチを切って開発

しかし今回のプロジェクトは、個人開発かつ「管理画面を通じた記事の追加」が主目的であるため、**現在は `main` ブランチで直接データ・記事を登録する運用**を採用しています。

### 運用上このようにしている理由

- **venv環境やSQLiteのDBをブランチ切替ごとに初期化したくない**  
（GitHub Codespacesの仕様上、それらが消えてしまうことがあるため）
- **データベースに登録された記事をそのまま継続利用したいため、環境・DBの保持を優先**
- **開発と執筆が密接に結びついている**ため、ブランチ分割による恩恵が小さい

Developed by [Nubatan10001](https://github.com/Nubatan10001).
