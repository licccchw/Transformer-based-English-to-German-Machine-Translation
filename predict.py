from transformer_en_de.module import MTTransformer

model = MTTransformer()
src_texts = [
    'Never put off what you can do today until tomorrow.',
    'The change was for the better; I eat well, I exercise, I take my drugs.',
    'Such experiments are not conducted for ethical reasons.',
]
n_best = 1  # 每个输入样本的输出候选句子数量
trg_texts = model.predict(src_texts, n_best=n_best)
print(trg_texts)
for idx, st in enumerate(src_texts):
    print('-' * 30)
    print(f'src: {st}')
    for i in range(n_best):
        print(f'trg[{i + 1}]: {trg_texts[idx * n_best + i]}')
