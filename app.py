from flask import Flask, render_template, request,  session, redirect, url_for

app = Flask(__name__)

my_list = []
completed_list = []


@app.route('/')
def index():
    return render_template('index.html', my_list=my_list, completed_list=completed_list)


@app.route('/add', methods=['POST'])
def add_item():
    new_item = request.form['new_item']
    my_list.append({'item': new_item, 'checked': False})
    return redirect(url_for('index'))


@app.route('/remove/<int:item_index>')
def remove_item(item_index):
    if 0 <= item_index < len(my_list):
        del my_list[item_index]
    return redirect(url_for('index'))


@app.route('/toggle/<int:item_index>')
def toggle_item(item_index):
    if 0 <= item_index < len(my_list):
        my_list[item_index]['checked'] = not my_list[item_index]['checked']
    return redirect(url_for('index'))


@app.route('/complete/<int:item_index>')
def complete_item(item_index):
    if 0 <= item_index < len(my_list) and not my_list[item_index]['checked']:
        completed_list.append(my_list.pop(item_index))
    return redirect(url_for('index'))


@app.route('/uncomplete/<int:item_index>')
def uncomplete_item(item_index):
    if 0 <= item_index < len(completed_list):
        my_list.append(completed_list.pop(item_index))
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=50008, debug=True)