import re
import matplotlib.pyplot as plt

# Read logs from logs.txt
with open("logs.log", "r") as file:
    logs = file.read()


# Regular expression to extract metrics
pattern = re.compile(
    r".*?- accuracy: (\d+\.\d+) - dice_coefficient: (\d+\.\d+) - jaccard_index: (\d+\.\d+) - loss: (\d+\.\d+) - val_accuracy: (\d+\.\d+) - val_dice_coefficient: (\d+\.\d+) - val_jaccard_index: (\d+\.\d+) - val_loss: (\d+\.\d+)"
)

# Lists to store metrics
epochs = []
accuracy, dice_coefficient, jaccard_index, loss = [], [], [], []
val_accuracy, val_dice_coefficient, val_jaccard_index, val_loss = [], [], [], []
i = 0
# Extract metrics from logs
for match in pattern.finditer(logs):
    i += 1
    acc, dice, jaccard, loss_val, val_acc, val_dice, val_jaccard, val_loss_val = match.groups()
    epochs.append(int(i))
    accuracy.append(float(acc))
    dice_coefficient.append(float(dice))
    jaccard_index.append(float(jaccard))
    loss.append(float(loss_val))
    val_accuracy.append(float(val_acc))
    val_dice_coefficient.append(float(val_dice))
    val_jaccard_index.append(float(val_jaccard))
    val_loss.append(float(val_loss_val))

# Plot metrics for the first 75 epochs
epochs = epochs[:75]
accuracy = accuracy[:75]
dice_coefficient = dice_coefficient[:75]
jaccard_index = jaccard_index[:75]
loss = loss[:75]
val_accuracy = val_accuracy[:75]
val_dice_coefficient = val_dice_coefficient[:75]
val_jaccard_index = val_jaccard_index[:75]
val_loss = val_loss[:75]

print(val_loss)
# Plot each metric
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(epochs, accuracy, label="Train Accuracy")
plt.plot(epochs, val_accuracy, label="Validation Accuracy", linestyle="--")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.title("Accuracy")

plt.subplot(2, 2, 2)
plt.plot(epochs, dice_coefficient, label="Train Dice Coefficient")
plt.plot(epochs, val_dice_coefficient, label="Validation Dice Coefficient", linestyle="--")
plt.xlabel("Epochs")
plt.ylabel("Dice Coefficient")
plt.legend()
plt.title("Dice Coefficient")

plt.subplot(2, 2, 3)
plt.plot(epochs, jaccard_index, label="Train Jaccard Index")
plt.plot(epochs, val_jaccard_index, label="Validation Jaccard Index", linestyle="--")
plt.xlabel("Epochs")
plt.ylabel("Jaccard Index")
plt.legend()
plt.title("Jaccard Index")

plt.subplot(2, 2, 4)
plt.plot(epochs, loss, label="Train Loss")
plt.plot(epochs, val_loss, label="Validation Loss", linestyle="--")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.title("Loss")

plt.tight_layout()
plt.show()
