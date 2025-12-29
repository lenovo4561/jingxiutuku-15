const sharp = require('sharp')
const path = require('path')
const fs = require('fs')

const logoPath = path.join(__dirname, '../src/assets/images/logo.png')
const outputPath = path.join(__dirname, '../src/assets/images/logo.png')

// 确保目录存在
const outputDir = path.dirname(outputPath)
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true })
}

sharp(logoPath)
  .resize(192, 192, {
    fit: 'cover',
    position: 'center'
  })
  .png({ quality: 90 })
  .toFile(outputPath + '.tmp')
  .then(() => {
    // 替换原文件
    fs.renameSync(outputPath + '.tmp', outputPath)
    console.log('✅ Logo 已成功压缩为 192x192')
  })
  .catch(err => {
    console.error('❌ Logo 压缩失败:', err)
    process.exit(1)
  })
