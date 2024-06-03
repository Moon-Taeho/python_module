# Python モジュールについて

Python で他のモジュールの関数や変数を使用する方法には、`import` と `from import` の 2 つの方法があります。それぞれの方法と使い分け、さらにモジュールを使用する理由やサンプルスクリプトについて解説します。

## 1. モジュールを使用する理由

モジュールを使うことにはいくつかのメリットがあります。

- コードの再利用性が高まります。
- 大規模なプログラムをモジュール単位で管理しやすくなります。
- 開発効率が向上します。

## 2. Import と from import の違い

- `import`：モジュール全体をインポートし、そのモジュール内の関数や変数を利用する際に使用します。

  ```python
  import module_name
  module_name.function_name()
  ```

- `from import`：指定したモジュールから一部の関数や変数だけを直接インポートして使用する際に使用します。

  ```python
  from module_name import function_name
  function_name()
  ```

## 3. 実際のスクリプト例

以下は、独自のモジュールを作成し、そのモジュール内の関数を主プログラムから利用する簡単な例です。

- `my_module.py` の中身

  ```python
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b
  ```

- `main.py` Import

  ```python
    import calc

    result1 = calc.add(10, 5)
    print(result1)

    result2 = calc.subtract(10, 5)
    print(result2)
  ```

- `main.py` From Import

  ```python
    from calc import add, subtract

    result1 = add(10, 5)
    print(result1)

    result2 = subtract(10, 5)
    print(result2)

  ```
