**SG2000 和 SG2002 的条件编译编码设计笔记**


SG2000 和 SG2002 不同的地方可以采用 Sphinx 支持的条件编译方式进行编码。具体方式如下：

- 条件编译文字

  ```rst
  .. only:: sg2002

          SG2002 ......

  .. only:: sg2000

          SG2000 ......
  ```

- 条件编译图片

  ```rst
  .. only:: sg2002

          .. _diagram_package_pins_sg2002:
          .. figure:: ../../../../media/image4.png

                  管脚分布图

  .. only:: sg2000

          .. _diagram_package_pins_sg2000:
          .. figure:: ../../../../media/image3.png

                  管脚分布图
  ```

  **注意：采用 only 语法时，不同条件下的 "锚点" id 必须不同，否则编译时会报错说有重复。**

- 条件编译 include 文件

  ```rst
  .. only:: sg2002

          .. include:: ./interrupts-sg2002.table.rst

  .. only:: sg2000

          .. include:: ./interrupts-sg2000.table.rst
  ```


项目中需要将 `"sg2002"` / `"sg2000"` 作为 tag 添加在 Makefile 中，具体可以参考 `SG200X/TRM/sg2000_cn/Makefile` 或者 `SG200X/TRM/sg2002_cn/Makefile`。

譬如 `SG200X/TRM/sg2002_cn/Makefile` 中，我们为 `SPHINXOPTS` 定义了 tag `"sg2002"` 如下：

```makefile
SPHINXOPTS    ?= -t sg2002
```

`SPHINXOPTS` 会在执行 `sphinx-build` 时作为命令行参数带入。

```makefile
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(BUILD_CONFIG) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```