from django import forms


class PostForm(forms.Form):
    image = forms.ImageField(label='イメージ画像',required=False) # 追加
    comment = forms.CharField(label='コメント', widget=forms.Textarea(),required=False)
    hashtag= forms.CharField(label='ハッシュタグ', widget=forms.Textarea(),required=False)
